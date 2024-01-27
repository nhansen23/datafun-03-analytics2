'''
Module 3 - Project 2: GitHub, Cloning, and Python practice

This file is for practice to import modules, fetch data and write to a file
'''

# Standard library imports
import csv
import pathlib
import statistics
import io
from pathlib import Path
from io import StringIO

# External library imports
import requests
import pandas as ps
  

# Local module imports
# import nicole_attr <- no idea what this means
import nicole_projsetup

'''
Function to fetch data

'''

# Fetch csv data
def fetch_and_write_csv_data(folder_name, filename, url):
    # print("FETCH AND WRITE FUNCTION: The csv directory is %s." % folder_name)
    # print("FETCH AND WRITE FUNCTION: The csv filename is %s." %filename)
    # print("FETCH AND WRITE FUNCTION: The csv URL is %s." %url)
    response = requests.get(url)
    if response.status_code == 200:
        # Pass directory and file information along with the file content
        write_csv_file (folder_name, filename, response.content)
    else:
        print(f"Failed to fetch csv data: {response.status_code}")
'''
# Fetch JSON data
def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Pass directory and file information along with the file content
        write_json_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch json data: {response.status_code}") 
'''

'''
# Fetch txt data
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file
    else:
        print(f"Failed to fetch txt data: {response.status_code}") 

# Fetch Excel data
def fetch_and_write_xlsx_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_xlsx_file
    else:
        print(f"Failed to fetch xlsx data: {response.status_code}") 
'''


'''
Functions to write the files

'''
# Write a csv file
def write_csv_file(folder_name, filename, data):
    print("WRITE FUNCTION: The csv directory is %s." % folder_name)
    print("WRITE FUNCTION: The csv filename is %s." % filename)
    print("WRITE FUNCTION: Data is %s." % data)
    
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join path

    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open('w', encoding='UTF8') as file:
        print(file)
        file.write(StringIO(data, '\n'))
        
        print(f"CSV data saved to {file_path}")

'''
# Write a JSON file
def write_json_file(folder_name, filename, data):
    print("WRITE FUNCTION: The csv directory is %s." % folder_name)
    print("WRITE FUNCTION: The csv filename is %s." % filename)
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join path
    
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open('w') as file:
        file.write(data)
        print(f"JSON data saved to {file_path}")    
'''
'''  
# Write a text file
def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join path
    
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

 # Write an Excel file   
def write_xlsx_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join path
    
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")
'''  

'''
Process data and generate ouput

'''

# Function 1: Process text data
# def process_txt_file(folder_name, txt_filename)
'''
# Function 2: Process CSV data
def process_csv_file(folder_name, csv_filename):
    file_path = Path(folder_name).joinpath(csv_filename)

    with file_path.open('r') as open_csv:
        open_csv = []
        for banks in open_csv:
            banks += 1
        print("The number of failed banks is %s." % banks)

    csv_output_path = Path(folder_name).joinpath(csv_output)
    with csv_output_path.open('w') as csv_output:
        csv_output.write()
        print(f"CSV file saved as text file to {csv_output_path}")   
        
'''
# Function 3: Process Excel data
#def process_xlsx_file(folder_name, xlsx_filename)

# Function 4: Process JSON data
#def process_json_file(folder_name, json_filename)


def main():
    '''Main function to fetch and write data from the web
       as well as process data from various file types.
    '''
    name_string = "Nicole"
    print(f"Name: {name_string}") # left out the name_attr ... still do not know what that is

# Assign url's to each file type
   #txt_url = 'https://nces.ed.gov/ccd/Data/zip/sdf21_1a.zip'
    # csv_url = 'https://github.com/GTB-TME/gtbreport2023/blob/main/data/mortality/dths_total.csv'
    csv_url = 'https://www.fdic.gov/bank/individual/failed/banklist.csv'
    #xlsx_url = 'https://irma.nps.gov/DataStore/DownloadFile/612238?Reference=2246102'
    json_url = 'https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.json?accessType=DOWNLOAD'

# Assign folder names for each file type
   # txt_folder_name = 'nces_data'
    csv_folder_name = 'csv-directory'
    #xlsx_folder_name = 'national_parks'
    json_folder_name = 'json-directory'

# Assign filenames for each file type
    #txt_filename = 'nces.txt'
    csv_filename = 'banks.csv'
    #xlsx_filename = 'bird_monitoring.xlsx'
    json_filename = 'chicago_crime.json'

# Fetch and write data
   # fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    #fetch_and_write_xlsx_data(xlsx_folder_name, xlsx_filename, xlsx_url)
    #fetch_and_write_json_data(json_folder_name, json_filename, json_url)

# Process the data
   # process_txt_file(txt_filename)
   # process_csv_file(csv_folder_name, csv_filename)
   # process_xlsx_file(xlsx_filename)
   # process_json_file(json_filename)

if __name__ == "__main__":
    main()
