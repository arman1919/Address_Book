from utils import is_valid_number,is_valid_date,is_valid_email

#Date_Descriptor

class Date_Descriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        
        if not is_valid_date(value):
            raise ValueError
        
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
#String Descriptor
class Str_Descriptor:
    
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        
        if not isinstance(value,str) or len(value) <= 1:
            raise ValueError
        
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__.get(self.name)

# Phone_Number_Descriptor

class Phone_Number_Descriptor:
    
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        
        if not is_valid_number(value):
            raise ValueError
        
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    
#Email_Number_Descriptor

class Email_Number_Descriptor:
    
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        
        if not is_valid_email(value):
            raise ValueError
        
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)


class Contact:
    
    name = Str_Descriptor()
    phone_number =  Phone_Number_Descriptor()
    email_address = Email_Number_Descriptor()
    birthday = Date_Descriptor()
    
    
    def __init__(self,name:str,phone_number:str,email_address:str,birthday:str) -> None:
        """
        Args:
            name (str): name user 
            phone_number (str): phone number user
            email_address (str): email address user 
            birthday (str): birthday  user "Day-Month-Year" 
            
        """
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.birthday = birthday
        
        
    def to_json(self):
        
        return {
            "name": self.name,
            "phone_number": self.phone_number,
            "email_address": self.email_address,
            "birthday": self.birthday
        }
        
        
    def __str__(self) -> str:
        return f"Name - {self.name}, phone_number - {self.phone_number}, email_address - {self.email_address}, birthday -{self.birthday}"

