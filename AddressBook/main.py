from address_book import Address_Book
import utils
import file_handler


def main():
    address_book = Address_Book()
    while True:
        print("-----------------------------")
        print("Enter opration")
        print("1) Add contact")
        print("2) Delete contact ")
        print("3) Update contact")
        print("4) Search contact")
        print("5) Creat address book json file")
        print("6) load address book file")
        print("0) Exit")
        print("-----------------------------")
        
        sel = int(input())
        
        if sel == 1:
            name = utils.name_inpit()
            
            while True:
                number = utils.phone_number_input()
                if number not in  address_book.contacts.keys():
                    
                    break
                
                print("the number already exists")
                
            while True:
                
                email = utils.email_input()
                j = 0
                for i in address_book.contacts.values():
                    if email == i.email_address:
                        j += 1
                if j > 0:
                    print("email already exists")
                else:
                    break
                
                
            birthday = utils.birthday_input()

            address_book.add_contact(name,number,email,birthday)
        
        elif sel == 2:
            while True:
                
                for contact in address_book.contacts.values():
                    print(f"name-{contact.name} phone number -{contact.phone_number} email - {contact.email_address} birthday - {contact.birthday}  ")
                
                i = input("Enter contact phone nuber for delete")

                if  i not in address_book.contacts:
                    
                    print("Number not fond")
                    
                else:
                    address_book.contacts.pop(i)
                    print("Сontact deleted")
                    break
                
        elif sel == 3:
            while True:
                
                for contact in address_book.contacts.values():
                    print(f"name-{contact.name} phone number -{contact.phone_number} email - {contact.email_address} birthday - {contact.birthday}  ")
                
                i = input("Enter contact phone nuber for update")

                if  i not in address_book.contacts:
                    
                    print("Number not fond")
                    
                else:
                    update_contact = address_book.contacts[i]
                    
                    choose_list =["name","phone_number","email_address","birthday"]
                    update_parametr = utils.selectin(choose_list)
                    
                    if update_parametr == "name":
                        new_name = utils.name_inpit()
                        
                        
                        address_book.update_contact(update_contact,update_parametr,new_name)
                        
                    elif update_parametr == "phone_number":
                        new_phone_number = utils.phone_number_input()
                        
                        address_book.update_contact(update_contact,update_parametr,new_phone_number)
                        
                    elif update_parametr == "email_address":
                        new_email_address = utils.email_input()
                        
                        address_book.update_contact(update_contact,update_parametr,new_email_address)
                    
                    elif update_parametr == "birthday":
                        new_birthday = utils.birthday_input()
                        
                        address_book.update_contact(update_contact,update_parametr,new_birthday)
                    
                        
                    
                    break
        
        elif sel == 4:
            
            choose_list =["name","phone_number","email_address","birthday"]
            search_parametr = utils.selectin(choose_list)  
            if search_parametr == "name":
                  
                name  = utils.name_inpit()
                  
                found_contacts = address_book.search_contact(search_parametr,name)
                if found_contacts == None:
                    print("Contacts not found")
                elif len (found_contacts) == 1:
                    print("contact found ")
                    print(found_contacts[0])
                else:
                    print(f"{len(found_contacts)} - contact found")
                    for i in found_contacts:
                        print(i)
            
            elif search_parametr == "phone_number":
                
                found_nuber = address_book.search_contact(search_parametr,None)
                if found_nuber == None:
                    print("Nuber not found")
                else:
                    print("contact found")
                    print(address_book.contacts[found_nuber])
                
            elif search_parametr == "email_address":
                found_email = address_book.search_contact(search_parametr,None)
                if found_email == None:
                    print("Nuber not found")
                else:
                    print("contact found")
                    print(found_email)
            
            elif search_parametr == "birthday":
                birthday  = utils.birthday_input()
                  
                found_contacts = address_book.search_contact(search_parametr,birthday)
                if found_contacts == None:
                    print("Contacts not found")
                elif len (found_contacts) == 1:
                    print("contact found ")
                    print(found_contacts[0])
                else:
                    print(f"{len(found_contacts)} - contact found")
                    for i in found_contacts:
                        print(i)
                        
                        
        elif sel == 5:
            file_name = input(("enter a name for the file - "))
            file_handler.create_address_book(address_book,file_name)
            
            
        
            
        elif sel == 6:
            
            address_book = file_handler.read_address_book()
            print("Address book generated") 
        
        elif sel == 0:
            break
        
        
        else:
            print("select again")
            
        
if __name__ == "__main__":
    main() 
    
    
    
