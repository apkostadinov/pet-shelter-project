"""
Pet Shelter Registry
=====================

This file is a basic program to keep track of the patients of a pet shelter.
This started as a final project for the CS50P course, led by David A. Malan.
The project was successfully submitted to CS50P on 10.06.2024.
Currently, it's developed for research purposes.

Author: Aleksandar Kostadinov
GitHub: Robbin-Banx

Location: Sofia, Bulgaria
Date: 10.06.2024
Last Modified: 30.12.2024

"""

import sys
import os
import sqlite3
from tabulate import tabulate
from classes import Patient
from configparser import ConfigParser

# Instantiate
config = ConfigParser()

# Construct the path to config.ini
config_file_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "Config", "config.ini"
)

# Parse existing file
config.read(config_file_path)

# Get database name from config file
database_name = config.get("section a", "database_name")
database_extension = config.get("section a", "database_extension")
database_folder = config.get("section a", "database_folder")

database_name_ext = database_name + "." + database_extension

database = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), database_folder, database_name_ext
)

patients_table = "patients"


def main():
    """Creates a file if one does not exist in the directory"""

    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {patients_table} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        species TEXT,
        gender TEXT,
        name TEXT,
        age INTEGER
        )"""
        )
        conn.commit()
    except FileExistsError:
        pass

    """If command line arguments are preset execute them, if not prompts user for action, executes selected action"""

    while True:

        if len(sys.argv) == 2:
            match sys.argv[1]:

                case "-r":
                    route = "read"

                case "-s":
                    route = "search"

                case "-w":
                    route = "write"

                case _:
                    sys.exit("Command-line input not recognized")

        else:
            route = input("Read, Search or Write to database?: ").lower()

        match route:
            case "read":

                with sqlite3.connect(database) as conn:
                    cursor = conn.cursor()

                    # Retrieve all data from the table
                    cursor.execute(f"SELECT * FROM {patients_table}")
                    rows = cursor.fetchall()

                    if rows:
                        # Fetch column names from the table
                        cursor.execute(f"PRAGMA table_info({patients_table})")
                        column_info = cursor.fetchall()
                        headers = [
                            col[1] for col in column_info
                        ]  # Column names are in the second field

                        # Print the table
                        print(
                            tabulate(
                                rows, headers=headers, showindex=False, tablefmt="grid"
                            )
                        )
                    else:
                        print("The database is empty")

            case "search":
                found_patient = search_base(input("Name to search: ").capitalize())
                if found_patient is not None:
                    print(found_patient)

                    type_of_change = input(
                        "Do you want to edit or remove patient? Type 'edit', 'remove' or 'exit'! : "
                    ).lower()

                    match type_of_change:

                        case "edit":
                            try:
                                edit_entry(found_patient)
                                break
                            except ValueError as er:
                                print(er)

                        case "remove":
                            remove_entry(found_patient)
                            break
                        case "exit":
                            sys.exit("Exiting.")
                        case _:
                            print("Input not recognized. Try again!")
                else:
                    print("No results found")
                    break

            case "write":
                create_entry()
                break

            case "exit":
                sys.exit()

            case _:
                print("Invalid choice. Type 'Read', 'Search', 'Write' or 'Exit'?")
                continue


def write_to_database(patient: Patient, silent: bool = False) -> None:
    # Replace these with the actual column names and values
    new_entry = {
        "species": patient.species,
        "gender": patient.gender,
        "name": patient.name,
        "age": patient.age,
    }

    # Build the SQL query dynamically
    columns = ", ".join(new_entry.keys())
    placeholders = ", ".join(["?"] * len(new_entry))
    values = tuple(new_entry.values())

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO {patients_table} ({columns}) VALUES ({placeholders})", values
        )
        conn.commit()

    if not silent:
        print("Write successful.")


def create_entry():

    while True:
        try:
            patient = Patient()
        except ValueError as er:
            print(er)
            if input("Do you want to try again? Type 'Y' or 'N'!").lower() == "y":
                continue
            else:
                break
        break

    while True:
        print(patient)
        confirmation = input(
            "Review data. Commit to database? Type 'Y' or 'N'! "
        ).lower()

        if confirmation == "y":
            write_to_database(patient)
            break
        elif confirmation == "n":
            patient.edit(silent=True)
        elif input("Exit program?Type 'Y' or 'N'! ").lower() == "y":
            sys.exit()
        else:
            continue


def search_base(search_condition, silent=False):
    found_items = []

    # Define your search column
    search_column = "name"

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()

        # Perform the search
        query = f"SELECT * FROM {patients_table} WHERE {search_column} = ?"
        cursor.execute(query, (search_condition,))
        rows = cursor.fetchall()

        for i in rows:
            patient_i = Patient(id=i[0], species=i[1], gender=i[2], name=i[3], age=i[4])
            found_items.append(patient_i)


    # Return search result
    if len(found_items) == 0:
        return None
    elif len(found_items) == 1:
        if not silent:
            print("Search Successful")
        return found_items[0]
    elif len(found_items) > 1:
        return multiple_search_results(found_items)


def multiple_search_results(found_items: list):
    # Handle cases where there are multiple found items from the search function
    user_input = None
    # Create indexing for found results
    for i in found_items:
        print(f'id: {i.id}', "|", f'{i}')

    while True:
        # Ask user which match is the correct one
        try:
            user_input = int(
                input(
                    "Which patient is the one you are looking for? Type the id number: "
                )
            )
        except ValueError:
            print("Please input an integer")

        for i in found_items:
            if i.id == user_input:
                return i
            else:
                continue
        else:
            print("Value not found.")


def edit_entry(patient):

    new_patient = patient.edit()

    # Define the criteria for identifying the row to update
    search_column = "id"  # The column used to find the specific row
    search_value = patient.id  # The value to search for in the column

    # Define the new values for the columns to update
    updated_data = {
        "species": new_patient.species,  # Replace with the actual column names and new values
        "gender": new_patient.gender,
        "name": new_patient.name,
        "age": new_patient.age,
    }

    # Build the SET clause dynamically
    set_clause = ", ".join([f"{col} = ?" for col in updated_data.keys()])
    values = list(updated_data.values()) + [
        search_value
    ]  # Add the search value to the parameters

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()

        # Update the row in the table
        query = f"UPDATE {patients_table} SET {set_clause} WHERE {search_column} = ?"
        cursor.execute(query, values)
        conn.commit()

        print("Row updated successfully!")


def remove_entry(patient, silent: bool = False):
    if patient.id:
        delete_column = "id"  # The column used to find the specific row
        delete_value = patient.id  # The value to match for deletion
    elif patient.name:
        delete_column = "name"  # The column used to find the specific row
        delete_value = patient.name  # The value to match for deletion


    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()

        # Delete the row from the table
        query = f"DELETE FROM {patients_table} WHERE {delete_column} = ?"
        cursor.execute(query, (delete_value,))
        conn.commit()

    if not silent:
        print("Patient removed")

if __name__ == "__main__":
    main()
