from contact import Contact
from parameter_search import parameter_search


class Address_Book:
    def __init__(self) -> None:
        self.contacts = {}
        
    def add_contact(self,name:str,phone_number:str,email_address:str,birthday:str) -> None:
        """
        Args:
            name (str): name user 
            phone_number (str): phone number user
            email_address (str): email address user 
            birthday (str): birthday  user "Day-Month-Year" 
            
        """
        
        new_contact = Contact(name,phone_number,email_address,birthday)
        
        self.contacts[new_contact.phone_number] = new_contact
        print("Contact added")
        
    
    def dell_contact(self,contact):
        if contact is None:
            print("the contact does not exist")
        
        else:
            self.contacts.pop(contact.phone_number)
            print(f"contact deleted")
        
    
        
    def search_contact(self,type_parametr,parametr):
        if type_parametr == "name":
            found_contacts = []
            for i in self.contacts.values():
                if i.name == parametr:
                    found_contacts.append(i)
            
            if len(found_contacts) == 0:
                return None
            else:
                return found_contacts
            
                                
            
        elif type_parametr == "phone_number":
            phone_numbers = []
            for i in self.contacts:
                phone_numbers.append(self.contacts[i].phone_number)
            
            found_parameters = parameter_search(phone_numbers)
            if len(found_parameters) == 0:
                return None
            else:
                return found_parameters[0]
            
            
        elif type_parametr == "email_address":
            email_addreses = []
            for i in self.contacts:
                email_addreses.append(self.contacts[i].email_address)
            
            found_parameters = parameter_search(email_addreses)
            if len(found_parameters) == 0:
                return None
            else:
                for i in self.contacts.values():
                    if i.email_address == found_parameters[0]:
                        return i
                
            
        
        
        elif type_parametr == "birthday":
            found_contacts = []
            for i in self.contacts.values():
                if i.birthday == parametr:
                    found_contacts.append(i)
            
            if len(found_contacts) == 0:
                return None
            else:
                return found_contacts
        
        
    def update_contact(self,contact,update_parametr_type,update_parametr):
        if update_parametr_type == "name":
            
            print(f"parametr  - {self.contacts[contact.phone_number].name} - update  -{update_parametr}")
            self.contacts[contact.phone_number].name = update_parametr
            
        elif update_parametr_type == "email_address":
            
            print(f"parametr  - {self.contacts[contact.phone_number].email_address} - update  -{update_parametr}")
            self.contacts[contact.phone_number].email_address = update_parametr
        
        elif update_parametr_type == "phone_number":
            
            print(f"parametr  - {self.contacts[contact.phone_number].phone_number} - update  -{update_parametr}")
            self.contacts[contact.phone_number].phone_number = update_parametr
            
        elif update_parametr_type == "birthday":
            
            print(f"parametr  - {self.contacts[contact.phone_number].birthday} - update  -{update_parametr}")
            self.contacts[contact.phone_number].birthday = update_parametr
            

