import os
from pathlib import Path
import logging

project_name = "LoanApproval"

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')
file_paths = [
    ".github/workflows/main.yml",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/logging/__init__.py",
    f"{project_name}/logging/logger.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",
    f"{project_name}/cloud/__init__.py",
    "dataset/",
    "notebook/",
    "logs/",
    "config/config.yml",
    "data_schema/schema.yml",
    "params.yml",
    "schema.yml",
    "Dockerfile",
    "setup.py",
    "main.py",
    "requirements.txt",
    ".env"
]

for file_path in file_paths:

    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating the directory {file_dir}")

    if file_name != "" and (not os.path.exists(file_path) or os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            logging.info(f"Creating the file {file_name}")
    else:
        logging.info(f"{file_name} File Already Exist")