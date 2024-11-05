import logging
import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
from LoanApproval.entity.config_entity import DataIngestionConfig
from LoanApproval.exception.exception import CustomException

from  LoanApproval.entity.artifact_entity import DataIngestionArtifact
load_dotenv()

# Accessing the environment variables
mongo_db_username = os.getenv('mongo_db_username')
mongo_db_password = os.getenv('mongo_db_password')



MONGO_DB_URI = "mongodb+srv://"+ mongo_db_username+ ":" + mongo_db_password + "@loanapprovalmongobd.rridu.mongodb.net/?retryWrites=true&w=majority&appName=LoanApprovalMongoBD"

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise  CustomException(e,sys)

    def load_mongodb_collection_df(self):
        """
        It will be going to load the collection data form mongodb,
        convert it into dataframe,
        remove the extract _id columns
        :return: read_df
        """
        try:
            mongodb_name = self.data_ingestion_config.data_ingestion_db
            mongodb_collection = self.data_ingestion_config.data_ingestion_collection
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI)
            mongodb_collection_data = self.mongo_client[mongodb_name][mongodb_collection]

            read_df = pd.DataFrame(list(mongodb_collection_data.find()))

            if "_id" in read_df.columns.to_list():
                read_df.drop(columns=["_id"], axis=1, inplace=True)

            #read_df.replace({"na", np.nan}, inplace=True)

            return read_df
        except Exception as e:
            raise CustomException(e, sys)

    def export_raw_ds_feature_store(self,  load_df: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            feature_store_dir = os.path.dirname(feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)
            print("----------------",feature_store_file_path, load_df)
            load_df.to_csv(feature_store_file_path, index=False, header=True)
            return load_df

        except Exception as e:
            raise CustomException(e, sys)

    def train_test_split_df(self, load_df: pd.DataFrame):
        try:
            train_df, test_df = train_test_split(
                load_df, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Splitting the Dataset into training and test set")

            train_dir = os.path.dirname(self.data_ingestion_config.training_file_path)

            os.makedirs(train_dir, exist_ok=True)

            logging.info("Exporting the training and testing set")

            train_df.to_csv(
                self.data_ingestion_config.training_file_path, index= False, header= True
            )
            test_df.to_csv(
                self.data_ingestion_config.test_file_path, index= False, header= True
            )
        except Exception as e:
            raise CustomException(e, sys)
    def init_data_ingestion(self):
        try:
            load_df = self.load_mongodb_collection_df()

            load_df = self.export_raw_ds_feature_store(load_df)

            self.train_test_split_df(load_df)

            data_ingestion_artifact = DataIngestionArtifact(train_file_path_artifact=self.data_ingestion_config.training_file_path,
                                                            test_file_path_artifact=self.data_ingestion_config.test_file_path)
            return  data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys)