# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08- Main Script
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# S.Foley,3.12.2024,Modified Script for Assignment 8
# ------------------------------------------------------------------------------------------------- #

import json
from datetime import date
import data_classes as dataclass
import processing_classes as process
import presentation_classes as present

# Beginning of the main body of this script
employees = process.FileProcessor.read_employee_data_from_file(file_name=dataclass.FILE_NAME,
                                                       employee_data=dataclass.employees,
                                                       employee_type=dataclass.Employee)  # Note this is the class name (ignore the warning)

# Repeat the follow tasks
while True:
    present.IO.output_menu(menu=dataclass.MENU)

    menu_choice = present.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            present.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            present.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = present.IO.input_employee_data(employee_data=employees, employee_type=dataclass.Employee)  # Note this is the class name (ignore the warning)
            present.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            present.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            process.FileProcessor.write_employee_data_to_file(file_name=dataclass.FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {dataclass.FILE_NAME} file.")
        except Exception as e:
            present.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
