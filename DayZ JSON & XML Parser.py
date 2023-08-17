'''
DayZ JSON & XML Parser 
Made for use with DayZ. Scans folders and subfolders for json and xml files, scanning them for errors and creating a log file in /downloads. 
Quick easy way to locate issues as dayz print to script there's an invalid json or xml, but never tell you which one is invalid. 

''' 
__author__ = "naps"
__copyright__ = "Copyright (C) 2023 Nick Shepherd"
__license__ = "General Public License v3.0"
__version__ = "1.0"

import os
import json
import xml.etree.ElementTree as ET

def validate_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        return None
    except Exception as e:
        return str(e)

def validate_xml(file_path):
    try:
        with open(file_path, 'r') as file:
            ET.parse(file)
        return None
    except Exception as e:
        return str(e)

def check_folder_for_invalid_files(folder_path, log_file):
    for root, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            error_message = None

            if file.endswith('.json'):
                error_message = validate_json(file_path)
            elif file.endswith('.xml'):
                error_message = validate_xml(file_path)

            if error_message:
                log_message = f"File: {file_path}, Error: {error_message}\n"
                log_file.write(log_message)

def main():
    target_folder = r"Path-to-server-folder"  # Replace with the folder path to check
    log_file_path = os.path.join(os.path.expanduser("~"), "Downloads", "validation_log.txt")

    with open(log_file_path, 'w') as log_file:
        check_folder_for_invalid_files(target_folder, log_file)

if __name__ == "__main__":
    main()
