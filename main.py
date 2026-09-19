from animals import Cats, Dogs, Birds, Snakes
from shelter import Shelter
from people import Adopter

from exceptions import (
    AnimalNotFound,
    TooManyAnimal,
    IdNotValid,
    PhoneNumberNotValid,
    duplicateAnimal
)


shelter = Shelter()
#put all the created adopter in a list
adopters = []


def create_animal():
    print("\nChoose animal type:")
    print("1. Cat")
    print("2. Dog")
    print("3. Bird")
    print("4. Snake")

    choice = input("Enter your choice: ").strip()

    name = input("Animal name: ").strip()
    age = input("Animal age: ").strip()
    gender = input("Animal gender: ").strip()
    breed = input("Animal breed: ").strip()

    if choice == "1":
        animal = Cats(name, age, gender, breed)

    elif choice == "2":
        animal = Dogs(name, age, gender, breed)

    elif choice == "3":
        animal = Birds(name, age, gender, breed)

    elif choice == "4":
        animal = Snakes(name, age, gender, breed)

    else:
        print("Invalid animal type.")
        return

    try:
        shelter.add_animal(animal)

    except duplicateAnimal as error:
        print(error)


def search_animal():
    print("\n1. Search by name")
    print("2. Search by breed")

    choice = input("Choose: ")

    try:
        if choice == "1":
            name = input("Enter animal name: ").strip()
            shelter.search_animal(name)

        elif choice == "2":
            breed = input("Enter animal breed: ").strip()
            shelter.search_by_breed(breed)

        else:
            print("Invalid choice.")

    except AnimalNotFound as error:
        print(error)


def get_or_create_adopter():
    name = input("Your name: ").strip()
    # check if adopter already exists if not create a new adopter and validate the phone number and national id
    for adopter in adopters:
        if adopter.name == name:
            return adopter

    adopter = Adopter(name)

    number = input("Phone number: ").strip()
    national_id = input("National ID: ").strip()

    try:
        adopter.validate(number, national_id)

        adopters.append(adopter)

        print("Adopter registered successfully!")

        return adopter

    except PhoneNumberNotValid as error:
        print(error)

    except IdNotValid as error:
        print(error)

    return None


def adopt_animal():
    adopter = get_or_create_adopter()
    # add animal to adopter's list of adopted animals and remove it from the shelter's list of available animals

    if adopter is None:
        return

    name = input("Enter the animal name you want to adopt: ")

    try:
        adopter.adopt(name, shelter)

    except AnimalNotFound as error:
        print(error)

    except TooManyAnimal as error:
        print(error)


def return_animal():
    # return an animal by name to the shelter and remove it from the adopter's list of adopted animals
    name = input("Your name: ").strip()

    adopter_found = None

    for adopter in adopters:
        if adopter.name == name:
            adopter_found = adopter
            break

    if adopter_found is None:
        print("Adopter not found.")
        return

    animal_name = input("Enter the animal name you want to return: ").strip()

    try:
        adopter_found.return_animal(
            animal_name,
            shelter
        )

    except AnimalNotFound as error:
        print(error)


def show_available_animals():
    shelter.show_animals()


def show_adopted_animals():
    shelter.my_adopted_animals()


while True:
    print("\n===== PET SHELTER =====")
    print("1. Add Animal")
    print("2. Show Animals")
    print("3. Search Animal")
    print("4. Adopt Animal")
    print("5. Return Animal")
    print("6. Show Available Animals")
    print("7. Show Adopted Animals")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_animal()

    elif choice == "2":
        shelter.show_animals()

    elif choice == "3":
        search_animal()

    elif choice == "4":
        adopt_animal()

    elif choice == "5":
        return_animal()

    elif choice == "6":
        show_available_animals()

    elif choice == "7":
        show_adopted_animals()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")