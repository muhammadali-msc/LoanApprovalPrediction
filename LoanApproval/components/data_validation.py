import logging
import os
import sys
import numpy as np
import pandas as pd

from LoanApproval.entity.config_entity import DataValidationConfig
from LoanApproval.exception.exception import CustomException

from  LoanApproval.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact

from scipy.stats import ks_2samp

from LoanApproval.constant.training_pipeline import SCHEMA_FILE_PATH

from LoanApproval.utils.utils import read_yaml_file, write_yaml_file
class DataValidation:
    def __init__(self, data_ingestion_artifact : DataIngestionArtifact, data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise CustomException(e, sys)

    def validate_data_cols(self, load_df: pd.DataFrame) -> bool:
        try:
            schema_config = self._schema_config
            load_df_col = load_df.columns
            if len(load_df_col) == len(schema_config):
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)

    def detect_data_drift(self, base_df, test_df, threshold = 0.05) -> bool:
        try:
            status = True
            report = {}
            for col in base_df.columns:
                base_data_col = base_df[col]
                load_data_col = test_df[col]
                equal_dist = ks_2samp(base_data_col, load_data_col)
                if equal_dist.pvalue >= threshold:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report.update({
                    col:{
                        "p_value": float(equal_dist.pvalue),
                        "drift_status": is_found
                    }
                })
            data_drift_path = self.data_validation_config.data_validation_drift_report_dir

            data_drift_dir = os.path.dirname(data_drift_path)
            os.makedirs(data_drift_dir, exist_ok=True)

            write_yaml_file(data_drift_path, report)

            return status
        except Exception as e:
            raise CustomException(e, sys)
    def init_data_validation(self) -> DataValidationArtifact:
        try:
            training_path = self.data_ingestion_artifact.train_file_path_artifact
            test_path = self.data_ingestion_artifact.test_file_path_artifact

            train_df = pd.read_csv(training_path)
            test_df = pd.read_csv(test_path)

            schema_status_train = self.validate_data_cols(train_df)

            if not schema_status_train:
                error_msg = "Training Columns Issue"

            schema_status_test = self.validate_data_cols(test_df)

            if not schema_status_test:
                error_msg = "Testing Columns Issue"

            status = self.detect_data_drift(base_df=train_df, test_df=test_df)

            valid_data_training_path = self.data_validation_config.data_validation_training_path
            valid_data_training_dir = os.path.dirname(valid_data_training_path)
            os.makedirs(valid_data_training_dir, exist_ok=True)

            train_df.to_csv(valid_data_training_path, index = False, header = True)

            valid_data_test_path = self.data_validation_config.data_validation_test_path
            test_df.to_csv(valid_data_test_path, index = False, header = True)

            data_validation_artifact = DataValidationArtifact(
                validation_status = status,
                valid_training_path = self.data_ingestion_artifact.train_file_path_artifact,
                valid_test_path= self.data_validation_config.data_validation_test_path,
                invalid_training_path= None,
                invalid_test_path= None,
                drift_report_path= self.data_validation_config.data_validation_drift_report_dir
            )
            return data_validation_artifact
        except Exception as e:
            raise CustomException(e, sys)