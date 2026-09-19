from exceptions import duplicateAnimal, AnimalNotFound


class Shelter:
    def __init__(self):
        self.all_animals = []
        self.adopted_animals = []

    def add_animal(self, animal_object):
        # check if the animal already exists in the shelter if so raise duplicateAnimal error
        for animal in self.all_animals:
            if animal.name == animal_object.name and animal.breed == animal_object.breed:
                raise duplicateAnimal(
                    "This animal is already in the shelter"
                )
        #else add the animal to the shelter
        self.all_animals.append(animal_object)

        print(f"{animal_object.name} was added successfully!")

    def show_animals(self):
        if not self.all_animals:
            #if list is empty print no available animals
            print("There are no available animals.")
            return
        #else loop through the list and print the animal info
        for i, animal in enumerate(self.all_animals):
            print(f"{i + 1}:")
            animal.show_info

    def search_animal(self, name):
        """search for an animal by name and return the animal object if found, else raise AnimalNotFound error"""
        for animal in self.all_animals:
            if animal.name == name:
                animal.show_info
                return animal

        raise AnimalNotFound(
            f"Animal '{name}' was not found"
        )

    def search_by_breed(self, breed):
        """same as search_animal but search by breed instead of name"""
        found = False

        for animal in self.all_animals:
            if animal.breed == breed:
                animal.show_info
                found = True

        if not found:
            raise AnimalNotFound(
                f"No animal with breed '{breed}' was found"
            )

    def my_adopted_animals(self):
        # list of my adopted animals
        if not self.adopted_animals:
            print("There are no adopted animals.")
            return

        for i, animal in enumerate(self.adopted_animals):
            print(f"{i + 1}:")
            animal.show_info

    def need_to_be_put_down(self):
        pass



