import re


class Patient:
    """"
    A class used to represent types of patients.

    """

    def __init__(
            self, species: str = None, gender: str = None, name: str = None, age: int = None, id: int = None
    ):
        if species != None:
            self.species = species
        else:
            self.species = input("What is the patient's species? ").capitalize()

        if gender != None:
            self.gender = gender.lower()
        else:
            self.gender = input("What is the patient male or female? ").lower()

        if name != None:
            self.name = name
        else:
            self.name = input("What is patient's name? ").capitalize()

        if age != None:
            self.age = age
        else:
            self.age = input("What's the patient's age? ")

        if id != None:
            self.id = id
        else:
            self.id = None

    def __str__(self):
        return str(
            f"Patient is a {self.gender} {self.species}. Patient's name is {self.name} and is {self.age} years old.")

    def __iter__(self):
        yield "Species", self.species
        yield "Gender", self.gender
        yield "Name", self.name
        yield "Age", self.age

    def __eq__(self, other):
        # don't attempt to compare against unrelated types
        if not isinstance(other, Patient):
            return NotImplemented

        return (
                self.species == other.species and
                self.gender == other.gender and
                self.name == other.name and
                self.age == other.age
        )

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if type(value) == int:
            self._id = value
        else:
            self._id = None

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        value = value.capitalize()
        if value == "Dog" or value == "Cat":
            self._species = value
        else:
            raise ValueError("Patient can be a dog or a cat.")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value == "male" or value == "female":
            self._gender = value
        else:
            raise ValueError("Patient must be male or female.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.search(r"\w+", value):
            self._name = value
        else:
            raise ValueError("Name must be at least one word")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        try:
            value = int(value)
            self._age = value
        except Exception:
            raise ValueError("Age must be a valid number")


    def edit(self, silent: bool = False):

        if silent == False:
            print(self)

        while True:
            match input("Do you want to edit species, gender, name or age?: ").lower():
                case "species":
                    if self.species == "Dog":
                        self.species = "Cat"
                        print("Species changed to Cat.")
                        break
                    elif self.species == "Cat":
                        self.species = "Dog"
                        print("Species changed to Dog.")
                        break
                case "gender":
                    if self.gender == "male":
                        self.gender = "female"
                        print("Gender changed to female.")
                        break
                    elif self.gender == "female":
                        self.gender = "male"
                        print("Gender changed to male.")
                        break
                case "name":
                    self.name = input("What is the new name?: ")
                    break
                case "age":
                    self.age = input("What is the new age?: ")
                    break
                case _:
                    print("Field not found")

        if silent == False:
            print("New description is: ", self)

        return self
