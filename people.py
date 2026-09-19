from exceptions import AnimalNotFound, TooManyAnimal, IdNotValid, PhoneNumberNotValid
import re


class Adopter:
    def __init__(self, name):
        self.name = name
        self.number = None
        self.id = None
        self.validated = False
        self.my_animals = []

    def validate(self, number, id):
        """validate the adopter's phone number and national id"""
        id_pattern = r"^\d{10}$"
        phone_pattern = r"^09\d{9}$"

        if re.fullmatch(id_pattern, id):
            self.id = id

            if re.fullmatch(phone_pattern, number):
                self.number = number
                self.validated = True

            else:
                raise PhoneNumberNotValid(
                    "The number is not valid. Make sure it starts with 09."
                )

        else:
            raise IdNotValid("Your ID is not valid!")

    def adopt(self, name, shelter):
        #adopt an animal by name from the shelter and add it to the adopter's list of adopted animals
        if len(self.my_animals) >= 9:
            raise TooManyAnimal(
                "You can't adopt any more animals"
            )

        for animal in shelter.all_animals:
            if animal.name == name:
                self.my_animals.append(animal)

                shelter.adopted_animals.append(animal)

                shelter.all_animals.remove(animal)

                animal.is_adopted = True

                return print(f"{animal.name} was adopted successfully!")

        raise AnimalNotFound(
            f"Animal '{name}' was not found"
        )

    def show_my_animals(self):
        # list of my adopted animals
        if not self.my_animals:
            print("You haven't adopted any animals.")
            return

        for i, animal in enumerate(self.my_animals):
            print(f"{i + 1}: {animal.show_info}")

    def return_animal(self, name, shelter):
        # return an animal by name to the shelter and remove it from the adopter's list of adopted animals
        for animal in self.my_animals:
            if animal.name == name:
                self.my_animals.remove(animal)

                shelter.adopted_animals.remove(animal)

                shelter.all_animals.append(animal)

                animal.is_adopted = False

                return print(f"{animal.name} was returned to the shelter!")

        raise AnimalNotFound(
            f"Animal '{name}' was not found in your adopted animals"
        )