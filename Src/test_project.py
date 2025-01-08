import pytest
from classes import Patient
from project import write_to_database
from project import search_base
from project import remove_entry
from project import database
from project import patients_table
import sqlite3


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    files_before = None
    # A test function will be run at this point
    yield
    # Code that will run after your test, for example:
    files_after = clean_up()
    assert files_after == True

def test_Patient_ValueError_for_species():

    with pytest.raises(ValueError, match="Patient can be a dog or a cat."):
        Patient("male", "male", "Harry", "4")

def test_Patient_ValueError_for_gender():

    with pytest.raises(ValueError, match="Patient must be male or female."):
        Patient("dog", "dog", "Harry", "4")

def test_Patient_ValueError_for_name():

    with pytest.raises(ValueError, match="Name must be at least one word"):
        Patient("dog", "male", "", "Harry")


def test_Patient_ValueError_for_age():

    with pytest.raises(ValueError, match="Age must be a number"):
        Patient("dog", "male", "Harry", "Harry")

def test_Patient_str():
    species = "Dog"
    gender = "male"
    name = "Harry"
    age = "4"
    test_patient = Patient(species, gender, name, age)
    assert str(test_patient) == f"Patient is a {gender} {species}. Patient's name is {name} and is {age} years old."

def test_Patient_eq_False():
    test_patient_1=Patient("dog", "male", "Harry", "4")
    test_patient_2=Patient("cat", "male", "Ronald", "4")
    assert (test_patient_1 == test_patient_2) == False

def test_Patient_eq_True():
    test_patient_1=Patient("dog", "male", "Harry", "4")
    test_patient_2=Patient("dog", "male", "Harry", "4")
    assert test_patient_1 == test_patient_2


def test_write_to_database():
    test_patient_1 = Patient("cat", "male", "Ronald", "4")
    write_to_database(test_patient_1, silent=True)
    subjects = []

    # Define your search criteria (e.g., column1 = "value1")
    search_column = "name"

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()

        # Perform the search
        query = f"SELECT * FROM {patients_table} WHERE {search_column} = ?"
        cursor.execute(query, (test_patient_1.name,))
        rows = cursor.fetchall()

        for i in rows:
            subjects.append(
                Patient(species=i[1], gender=i[2], name=i[3], age=i[4], id=i[0])
            )

    assert test_patient_1 in subjects


def test_search_database():
    test_patient_1 = Patient("cat", "male", "Christian", "4")
    write_to_database(test_patient_1, silent=True)
    result = search_base('Christian', silent=True)
    remove_entry(test_patient_1, silent=True)
    assert result == test_patient_1

def test_remove_entry():
    test_patient_1 = Patient("cat", "male", "Evan", "4")
    write_to_database(test_patient_1, silent=True)
    remove_entry(test_patient_1, silent=True)

    assert search_base(test_patient_1.name) == None


def clean_up():
    delete_column = "name"  # The column used to find the specific row
    delete_value = "Evan", "Ronald", "Christian"  # The value to match for deletion
    for i in delete_value:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()

            # Delete the row from the table
            query = f"DELETE FROM {patients_table} WHERE {delete_column} = ?"
            cursor.execute(query, (i,))
            conn.commit()

    return True
