import os
import sys
import numpy as np
import pandas as pd
'''Data Ingestion Related Constant'''
DATA_INGESTION_COLLECTION = "LoanApprovalCollection"
DATA_INGESTION_DATABASE = "LoanApprovalDB"
DATA_INGESTION_DIR = "data_ingestion"
DATA_INGESTION_FEATURE_STORE = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2

'''Training Pipeline Constant'''
TARGET_COL = 'loan_status'
PIPELINE_NAME: str = 'LoanApproval'
ARTIFACT_DIR: str = 'Artifacts'
FILE_NAME: str = 'LoanApprovalDataset.csv'

TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'

'''Data Validation Constant'''
DATA_VALID_DIR: str = "data_validation"
DATA_VALID_VALID_DIR: str = "validated"
DATA_VALID_INVALID_DIR: str = "invalid"
DATA_VALID_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALID_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yml")




