# Online Python-3 Compiler (Interpreter)
'''  
Purpose: Introduce Maverick Analytics  
''' 

import math 
import statistics 

#Create section break
section_break = "**************************************************"

#Company Information
company_name: str = "Maverick Analytics" 
short_description: str = "Customizing data visualizations to make an impact." 
employee_count: int = 5
is_large_company: bool = False

#Client Information
experience_sectors: list = ["K12 Education", "Higher Ed", "Healthcare", "Financial Services"] 
client_count_by_sector: list = [9, 3, 5, 4] 
client_count: int = sum(client_count_by_sector) 
client_employee_ratio: float = (client_count / employee_count)

#Customer Review Ratings
ratings: list = [5, 4, 5, 3, 4, 3, 4]
lowest_rating= min(ratings) 
highest_rating= max(ratings)
avg_rating = statistics.mean(ratings)
median_rating = statistics.median(ratings)

#f strings
employee_count_string: str = f"Number of Employees: {employee_count}"
is_large_company_string: str = f"Maverick Analytics is a large company: {is_large_company}"
experience_sectors_string: str = f"Experience in: {experience_sectors}"
client_count_string: str = f"Total Clients: {client_count}" 
client_employee_ratio_string: str = f"Client to Employee Ratio: {client_employee_ratio}"



ratings_string: str = f'''
Our Ratings: 
  Lowest Rating: {lowest_rating} 
  Highest Rating: {highest_rating} 
  Average Rating: {avg_rating}
  Median Rating: {median_rating}
'''

byline: str = f""" 
{section_break}
{company_name} 
{short_description}
{section_break}

{employee_count_string}
{is_large_company_string}

{experience_sectors_string}
{client_count_string} 
{client_employee_ratio_string}

{section_break}
{ratings_string}
""" 

def main(): 
#Display all output 
    print(section_break)
    print(company_name) 
    print(short_description)
    print(section_break)
    print()
    print(employee_count_string)
    print(is_large_company_string)
    print()
    print(experience_sectors_string)
    print(client_count_string) 
    print(client_employee_ratio_string)
    print()
    print(section_break)
    print(ratings_string)

    # If all of the above works, then the byline should work too: 
    print()
    print(byline) 

if __name__ == '__main__': 

    main() 
    
