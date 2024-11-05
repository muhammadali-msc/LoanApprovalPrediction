from datetime import datetime
import os
from LoanApproval.constant import training_pipeline

class TrainPipelineConfig:
    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp : str = timestamp

class DataIngestionConfig:
    def __init__(self, training_pipeline_config : TrainPipelineConfig ):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR
        )
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE, training_pipeline.FILE_NAME
        )
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
        )
        self.test_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
        )
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.data_ingestion_collection: str = training_pipeline.DATA_INGESTION_COLLECTION
        self.data_ingestion_db: str = training_pipeline.DATA_INGESTION_DATABASE

class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_VALID_DIR)
        self.data_validation_valid_dir = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALID_VALID_DIR)
        self.data_validation_invalid_dir = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALID_INVALID_DIR)
        self.data_validation_training_path = os.path.join(self.data_validation_valid_dir, training_pipeline.TRAIN_FILE_NAME)
        self.data_validation_test_path = os.path.join(self.data_validation_valid_dir, training_pipeline.TEST_FILE_NAME)
        self.data_invalidation_training_path = os.path.join(self.data_validation_invalid_dir, training_pipeline.TRAIN_FILE_NAME)
        self.data_invalidation_test_path = os.path.join(self.data_validation_invalid_dir,
                                                            training_pipeline.TEST_FILE_NAME)
        self.data_validation_drift_report_dir = os.path.join(self.data_validation_dir,
                                                             training_pipeline.DATA_VALID_DRIFT_REPORT_DIR,
                                                        training_pipeline.DATA_VALID_DRIFT_REPORT_FILE_NAME)