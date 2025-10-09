
# Pet Shelter Registry

*Author: Aleksandar Kostadinov

*GitHub: apkostadinov

*Location: Sofia, Bulgaria

*Date: 30.12.2024

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Operation](#operation)
- [Components](#components)

#### Description:
The project's main goal is to help create a registry for a pet shelter.
To achieve this the program creates a database file named "database.db" if one does not exist in the directory already. The name of the database can be changed on line 7 before starting the program.

#### Usage:

##### Interactive Mode
Upon starting the program the user is prompted for input. The user can:
* Type "read" to read the database, which will output the table for patients from the database file.
* Type "search" to search the table for patients and if a match is found the user can edit or remove the database entry by typing "edit" or "remove".
* Type "write" to add a new patient to the patient table of the "database.db" file.
* The user can also exit the program by typing "Exit".
* These inputs are not case sensitive.

##### Command-line mode:
* "patient.py -r" to read the patients table of the database.
* "patient.py -s" to search the database and if a match is found the user can edit or remove the database entry by typing "edit" or "remove". This will not change the order of the other entries.
* "patient.py -w" to add a new patient to the database.

#### Operation
The program operates by creating a patient object using the Patient class which contains the species, gender, name and age of the pet. Then depending on the context the object can be written to the database or be edited as a class instance by user prompts.

#### Components

##### Patient Class

The `Patient` class is used to represent the pets in the shelter. Each instance of the `Patient` class includes attributes for the species, gender, name, and age of the pet. The class provides methods for:

- Initializing a patient with given or prompted values.
- Generating a string description of the patient.
- Iterating over the patient's attributes to return them as a dictionary.
- Comparing two patient objects for equality based on their attributes.
- Editing the patient's attributes interactively.
- Storing the row id from the patient table in the database.

The `Patient` class is stored in the `classes.py` file.

 **Attributes:** `species`, `gender`, `name`, `age`, `id` 
 **Methods:**
    - `__str__`: Returns a description of the pet.
    - `__iter__`: Returns a dictionary where the keys are `"species"`, `"gender"`, `"name"`, and `"age"`, and the values are the corresponding strings or integers.
    - `__eq__`: Supports comparison of different instances.

##### Creating Objects

- **Interactive Mode:** Call the `Patient()` function. The user is prompted to input the necessary data for creating the object.
- **Search Mode:** When a search conducted and a result is found, the search function creates an object by calling `Patient("species", "gender", "name", "age", "id")` and returns the created object.

##### Main Function

The `main` function manages the primary workflow of the program. It ensures that the database file exists and handles user inputs through both command-line arguments and interactive prompts. The function supports reading the database, searching for and modifying entries, adding new patients to the database and editting existing entries.

##### Write Function

The `write_to_database` function takes a `Patient` class object and prompts the user to review the data. If confirmed, the patient data is written to the database. It provides an option to exit the program or retry the process. 

##### Create Entry

The `create_entry` function is used to initialize an instance object of the `Patient` class. It then asks for a confirmation from the user to write the entry to the database, edit the entry before it's written or exit the program.

##### Search Base Function

The `search_base` function searches the database for a patient by name. It returns the matching patient object if found, allowing further actions like editing or removal. The function handles cases with no results, single results, or multiple results.

##### Multiple Search Results Function

The `multiple_search_results` function is only called by the `search_base` function in scenarios where multiple patients match the search criteria. It prompts the user to select the correct patient from the list of found items and returns the chosen patient object for further actions.

##### Edit Entry Function

The `edit_entry` function allows editing of an existing patient's details. It takes an instance of the `Patient` class as argument then uses a class method of the `Patient` class to update the required information. The updated information is then passed to the database.

##### Remove Entry Function

The `remove_entry` function removes a specified patient from the database.  It takes an instance of the `Patient` class as argument it then uses the `patient.id` attribute to delete the entry from the patient table of the database.
