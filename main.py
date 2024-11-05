from LoanApproval.components.data_ingestion import DataIngestion
from LoanApproval.components.data_validation import DataValidation
from LoanApproval.exception.exception import CustomException
from LoanApproval.logging.logger import logging
from LoanApproval.entity.config_entity import DataIngestionConfig, DataValidationConfig
from LoanApproval.entity.config_entity import TrainPipelineConfig

import sys
import  os

from LoanApproval.utils.utils import read_yaml_file, write_yaml_file
from LoanApproval.constant.training_pipeline import SCHEMA_FILE_PATH


if __name__ == '__main__':
    try:

        train_pipline_config = TrainPipelineConfig()

        data_ingestion_config = DataIngestionConfig(train_pipline_config)

        data_ingestion = DataIngestion(data_ingestion_config)

        logging.info("Init Data Ingestion")
        data_ingestion_artifact = data_ingestion.init_data_ingestion()

        data_validation_config = DataValidationConfig(train_pipline_config)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
        data_validation_artifact = data_validation.init_data_validation()

        print(data_validation_artifact)

    except Exception as e:
        raise CustomException(e, sys)