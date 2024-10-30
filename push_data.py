import os
import sys
import json
import pandas as pd
import numpy as np
import pymongo
from LoanApproval.exception.exception import CustomException
from LoanApproval.logging.logger import logging
from dotenv import load_dotenv
import certifi

load_dotenv()
# Accessing the environment variables
mongo_db_username = os.getenv('mongo_db_username')
mongo_db_password = os.getenv('mongo_db_password')



uri = "mongodb+srv://"+ mongo_db_username+ ":" + mongo_db_password + "@loanapprovalmongobd.rridu.mongodb.net/?retryWrites=true&w=majority&appName=LoanApprovalMongoBD"

ca = certifi.where()


class LoanApprovalDataExtract():
    def __init__(self, database, collection):
        try:

            self.database = database
            self.collection = collection
            self.mongo_client = pymongo.MongoClient(uri)
        except Exception as e:
            raise CustomException(e,sys)

    def convert_csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e, sys)

    def insert_data_mongodb(self, records):
        try:
            self.records = records
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == '__main__':
    FILE_PATH = "dataset/LoanApprovalDataset.csv"
    DATABASE = "LoanApprovalDB"
    COLLECTION = "LoanApprovalCollection"

    network_data_extract_obj =  LoanApprovalDataExtract(DATABASE,COLLECTION)
    records_json = network_data_extract_obj.convert_csv_to_json(FILE_PATH)
    total_records =network_data_extract_obj.insert_data_mongodb(records_json)
    logging.INFO("Total Record insert into mongodb are: ", len(total_records))
