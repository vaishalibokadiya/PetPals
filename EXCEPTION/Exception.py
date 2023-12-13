class AgeException(Exception):
    def __init__(self, message="Age can't be negative"):
        self.message=message

class NullException(Exception):
    def __init__(self, message="An entity can't have null value"):
         self.message = message

class FundsException(Exception):
    def __init__(self, message="Donations can not be less than $10"):
         self.message = message

class FileException(Exception):
    def __init__(self, message="File not found or can't be read"):
         self.message = message

class AdoptionException(Exception):
    def __init__(self, message="Pet not available"):
         self.message = message
