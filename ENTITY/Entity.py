from abc import ABC, abstractmethod
from EXCEPTION import Exception
from UTIL import Util

class Pet:
    def __init__(self, name, age, breed):
        self.name = name

        if age<0:
            try:
                raise Exception.AgeException()
            except Exception.AgeException as e:
                print(e.message)
        self.age = age
        self.breed = breed

    def set_name(self):
        petName = input("Enter the pet's name")
        self.name = petName

    def set_age(self):
        age = int(input("Enter the pet's age"))
        if age<0:
            try:
                raise Exception.AgeException()
            except Exception.AgeException as e:
                print(e.message)
        self.age = age

    def set_breed(self):
        petBreed = input("Enter the pet's breed")
        self.breed = petBreed

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_breed(self):
        return self.breed
    
    def ToString(self):
        return (f'Pet\'s name: {self.name}, Pet\'s age: {self.age}, Pet\'s breed: {self.breed}')

class Dog(Pet):
    def __init__(self, name, age, breed, dogBreed):
        super().__init__(name, age, breed)
        self.dogBreed = dogBreed

    def set_dog_breed(self):
        dogBreed = input("Enter the dog's breed")
        self.dogBreed = dogBreed

    def get_dog_breed(self):
        return self.dogBreed
    
class Cat(Pet):
    def __init__(self, name, age, breed, catColor):
        super().__init__(name, age, breed)
        self.catColor = catColor

    def set_cat_color(self, catColor):
        catColor = input("Enter the cat's color")
        self.catColor = catColor

    def get_cat_color(self):
        return self.catColor

class PetShelter:
    availablePets = []
    def add_pet(pet):
        availablePets.append(pet)

    def remove_pet(pet):
        availablePets.remove(pet)

    def list_available_pets():
        for i in availablePets:
            print(i, end=", ")

class Donation(ABC):
    def __init__(self, donorName, amount):
        self.donorName = donorName
        if amount <10:
            try:
                raise Exception.FundsException()
            except Exception as e:
                print(e.message)
        self.amount = amount

    @abstractmethod
    def record_donation(self):
        pass

class CashDonation(Donation):
    def __init__(self, donorName, amount, donationDate):
        super().__init__(self, donorName, amount)
        self.donationDate = donationDate

    def record_donation(self):
        cursor=Util.DBConnUtil(Util.DBPropertyUtil())
        cursor.execute(f"USE PetPals; INSERT INTO donation VALUES ('{donorName}',{amount});")
        return print(cursor)

class ItemDonation(Donation):
    def __init__(self, donorName, amount, itemType):
        super().__init__(self, donorName, amount)
        self.itemType = itemType

    def record_donation(self):
        cursor=Util.DBConnUtil(Util.DBPropertyUtil())
        cursor.execute(f"USE PetPals; INSERT INTO donation VALUES ('{donorName}',{amount});")
        return print(cursor)

class IAdoptable(ABC):
    def Adopt():
        pass

class AdoptionEvent:
    def __init__(self, participants):
        self.participants = participants
    
    def host_event(self):
        print("Hosting an adoption event")

    def RegisterParticipant(self, participant):
        self.participants.append(participant)
    

