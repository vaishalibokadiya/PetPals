import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/PetPals/UTIL')
from Util import DBConnUtil,DBPropertyUtil

def record_donation():
    try:
        [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())

    except:
        return "Error in connection"
    else:
        donorName = input("Enter Donor name: ")
        amount = float(input("Enter Donation amount: "))
        try:
            mycursor.execute(f"INSERT INTO donation VALUES ('{donorName}',{amount});")
        except:
            print("Failed to insert data into the database.")
        else:
            print("Data inserted successfully.")

def register_participant():
    try:
        [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())

    except:
        return "Error in connection"
    else:
        participantName = input("Enter participant name: ")
        
        try:
            mycursor.execute(f"INSERT INTO participants VALUES ('{participantName}');")
        except:
            print("Failed to insert data into the database.")
        else:
            print("Data inserted successfully.")

def add_pet():
    try:
        [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())

    except:
        return "Error in connection"
    else:
        petName = input("Enter pet name: ")
        petAge = int(input("Enter pet's age: "))
        petBreed = input("Enter pet's breed: ")
        
        try:
            mycursor.execute(f"INSERT INTO pet VALUES ('{petName}','{petAge}','{petBreed}');")
        except:
            print("Failed to insert data into the database.")
        else:
            print("Data inserted successfully.")

def remove_pet():
    try:
        [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())

    except:
        return "Error in connection"
    else:       
        try:
            petName=input("Enter pet name: ")
            mycursor.execute(f"DELETE FROM pet WHERE name='{petName}';")
        except:
            print("Failed to delete data from the database.")
        else:
            print("Data deleted successfully.")


def list_available_pets():
    try:
        [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())

    except:
        return "Error in connection"
    else:       
        try:
            mycursor.execute("SELECT * FROM pet;")
            rows=mycursor.fetchall()
            for row in rows:
                print(row)
        except:
            print("Failed to fetch data from the database.")
        else:
            print("Data fetched successfully.")

def adoptionEventManagement():
    try:
        [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())

    except:
        return "Error in connection"
    else:       
        try:
            print("Hosting an event for the following participants: ")
            mycursor.execute("SELECT * FROM participants;")
            rows=mycursor.fetchall()
            for row in rows:
                print(row)
        except:
            print("Failed to fetch data from the database.")
        else:
            print("Data fetched successfully.")
