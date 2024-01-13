import readchar

def parameter_search(parameters):
    print("Enter something:")
    
    user_input = ""
    
    while True:

        char = readchar.readchar()
        
        
        contact_list = []
        user_input += char
        print(f"you have entered - {user_input}")
        
        
        for i in parameters:
            if user_input in i:
                print(i)
                contact_list.append(i)
                
        if len(contact_list) > 1:
            print("there are too many parameters")
        
        else:
            return contact_list
            



