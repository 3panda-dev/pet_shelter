from abc import ABC, abstractmethod

class Animals(ABC):
    """a animal class that is used to create different types of animals"""
    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.is_adopted = False

    @abstractmethod
    #must be implemented in the subclasses
    def speak(self):
        pass

    @abstractmethod
    #must be implemented in the subclasses
    def show_info(self):
        pass
    

class Cats(Animals):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, age, gender, breed)


    def speak(self):
        print("moew moew")


    @property
    def show_info(self):
        print(f"cat: \nname: {self.name}\nage: {self.age}\nrace: {self.gender}\nbreed: {self.breed}")

    def __str__(self):
        return "cats"


class Dogs(Animals):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, age, gender, breed)


    def speak(self):
        print("woof woof")

    @property
    def show_info(self):
        print(f"dog: \nname: {self.name}\nage: {self.age}\nrace: {self.gender}\nbreed: {self.breed}")

    def __str__(self):
        return "dogs"


class Birds(Animals):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, age, gender, breed)

    def speak(self):
        print("twik twik")

    @property
    def show_info(self):
        print(f"bird: \nname: {self.name}\nage: {self.age}\nrace: {self.gender}\nbreed: {self.breed}")

    def __str__(self):
        return "birds"
    


class Snakes(Animals):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, age, gender, breed)


    def speak(self):
        print("sisssss")


    @property
    def show_info(self):
        print(f"snake: \nname: {self.name}\nage: {self.age}\nrace: {self.gender}\nbreed: {self.breed}")


    def __str__(self):
        return "snakes"
    


