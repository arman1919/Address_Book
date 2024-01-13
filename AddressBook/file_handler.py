import json
from address_book import Address_Book

from  os import listdir
 


def create_address_book(adress_book,file_name):
    
    cotacts = []
    for i in adress_book.contacts:
        cotacts.append(adress_book.contacts[i].to_json())
    
    
    with open("data/"+file_name+".json", "w") as file:
        json.dump(cotacts, file)
    
    print("address book created")
    
    

def read_address_book():

    
    file_names = listdir("data/")
    address_book = Address_Book()
    
    
    while True:
        index = 1
        for i in file_names:
            print(f"{index})  {i} ")
            index +=1
        j = int(input("Enter index for file name - "))
        if j<0 or j > len(file_names):
            print("select again")
        else:
            file_name = file_names[j-1]
            
        
        
            with open("data/"+file_name, "r") as file:
                data = json.load(file)
    
            for contact in data:
                address_book.add_contact(contact["name"],contact["phone_number"],contact["email_address"],contact["birthday"])
        
            
            return address_book

         

