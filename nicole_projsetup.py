''' 
This module is used to practice looping and branching.
It provides functions for creating a series of project folders for
the data profiles.  It will create folders for each year plus
folders for the components of the data profile. 

'''

import math
import statistics
# import module from previous project: datafun-01-attr
import maverick_analytics


import pathlib 
from pathlib import Path

# Function to be called throughout
def create_directory(directory_name: str):# -> None: #no return type)
  '''
    Creates a directory to be used and re-used 
    for main directories and sub directories.
    
    :param directory_name: Name to be passed.
    '''
  pathlib.Path(directory_name).mkdir(exist_ok=True)


# Generate folders for a given year range
def create_folders_range(directory_name: str, start_year: int, end_year: int):
    create_directory(directory_name)
    for year in range(start_year, end_year + 1):
        year_folders = pathlib.Path(directory_name).joinpath(str(year))
        create_directory(year_folders)

# Generate folders from a provided list
def create_folders_list(directory_name: str, folder_list: list):
    create_directory(directory_name)
    for folder in folder_list:
        folder_levels = pathlib.Path(directory_name).joinpath(folder)
        create_directory(folder_levels)


# Generate suffixed folders by passing a list and adding a string to the end of the folder name
def create_suffixed_folders(directory_name: str, folder_list: list, suffix: str):
    create_directory(directory_name)
    for folder_name in folder_list:
        folder_suffix = pathlib.Path(directory_name).joinpath(f"{folder_name}{suffix}")
        create_directory(folder_suffix)
        #print(f"{folder_name} - {suffix}")


# Generate folders with a while loop
def create_folders_periodically(directory_name: str, duration):
    pathlib.Path(directory_name)
    create_directory(directory_name)
  

def main():
    
    # Print the byline from maverick_analytics module
    print(f"Byline: {maverick_analytics.byline}")

    # Create the year sub directories
    create_folders_range('dataProfiles', start_year=2018, end_year=2024)
    
    # Create folders from a list
    folder_list = ['Elementary School', 'Middle School','High School']
    create_folders_list(directory_name='Grade Levels', folder_list=folder_list)
    
    
    # Create the directories for S1 for each semester test
    folder_list = ['Biology','Chemistry','Algebra 1', 'Geometry','English 1','English 2']
    suffix = ' - S1'
    create_suffixed_folders('Semester Tests', folder_list, suffix)
  
    
    # Create folders in a loop
    create_folders_periodically('State Assessments', 5)
  

if __name__ == '__main__':
    main()



