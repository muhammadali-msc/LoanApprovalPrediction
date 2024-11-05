from dataclasses import  dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path_artifact: str
    test_file_path_artifact: str
@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_training_path: str
    valid_test_path: str
    invalid_training_path: str
    invalid_test_path: str
    drift_report_path: str