
#Shoe class
class Shoe():
    #defining attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #get cost method
    def get_cost(self):
        return self.cost
    
    # get quantity method
    def get_quantity(self):
        return self.quantity
    
    #to return a string representation of the class
    def __str__(self):
        return f"model: {self.product}, cost: ${self.cost}, quantity: {self.quantity}, ID: {self.code}"
    
collection = []

def read_shoes_data():
    #checking if the file exists
    try:
        with open('inventory.txt', 'r') as f:
            #reading the contents in the file
            info = f.readlines()
            #getting rid of the first line of data.
            info.pop(0)
            #iterating over each line of data and creating a shoe object.
            for item in info:
                data = item.split(',')
                country = data[0]
                code = data[1]
                product = data[2]
                cost = data[3]
                #stripping the '\n' so quantity can be turned into a int to perform arithmetic
                quantity = data[4]
                shoe_object = Shoe(country, code, product, cost, quantity.replace('\n',""))
                collection.append(shoe_object)
    #and if file does not exist.
    except FileNotFoundError:
        print('File does not exist')

def capture_shoes():    

    while True:
        try:
            #creating a object using the user input and appending it to the collection
            country = input('Country: ')
            code = input('Code: ')
            product = input('Product: ')
            cost = input('Cost: ')
            quantity = input('Quantity: ')
            shoe_object = Shoe(country, code, product, cost, quantity)
            collection.append(shoe_object)
            
                            
        except Exception:
            print('invalid input')
            continue
        
        try:
            #
            with open('inventory.txt', 'a+') as f:
                f.write(f"{country},{code},{product},{cost},{quantity}\n")
                break

        except FileNotFoundError:
            print('File does not Exist.')
            continue

def view_all():
    #iterating over the objects in the collection list
    for shoe in collection:
        #printing each object.
        print(shoe)

def re_stock():
    lst = []
    for shoe in collection:
       #transfering the quantity attribute to a int so can compare values to check for the lowest value.
       lst.append(int(shoe.quantity))

    for shoe in collection:
        if f"{min(lst)}" == shoe.quantity:
            while True:
                #checking user input.
                try:
                    print(shoe)
                    user_input = input(f"to update the quantity of {shoe.product}, {shoe.code} type 'yes': ")
                    if user_input.lower() == 'yes':
                            try:
                                user_input2 = int(input('Enter the new quantity amount: '))
                                with open('inventory.txt', 'r') as f:
                                #reading the contents in the file
                                    info = f.readlines()
                                    for i in range(len(info)):
                                        data = info[i].split(',')
                                        code = data[1]
                                        #checking if the right shoe is being updated
                                        if code == shoe.code:
                                            #changing the quantity of the shoe. and introducing '\n' because it's the last value of the string.
                                            data[4] = f"{user_input2}\n"
                                            new_data = ",".join(data)
                                            info[i] = new_data
                                    with open('inventory.txt', 'w') as f:
                                            for shoes in info:
                                                f.write(shoes)
                                                
                                        
                            except Exception:
                                print('please Enter a number')
                                continue
                    
                    #to ignore any other possible inputs.
                    break
                    
                    
                
                except Exception:
                    print('Opps wrong input, either type Yes or No')
                    continue
            break
                  
def shoe_search():
    #getting user input
    user_code = input('Enter shoe code: ').lower()
    #checking if there is elements in the list.
   
        #iterating over each object.
    for i in range(len(collection)):
        shoe = collection[i]
        if user_code == shoe.code.lower():
            #returning the shoe searched for.
            print(shoe)
            break
        
def value_per_item():
    for shoe in collection:
        print(f"shoe: {shoe.product}, value: ${int(shoe.cost) * int(shoe.quantity)}")
        

def highest_qty():
    
    lst = []
    for shoe in collection:
       #transfering the quantity attribute to a int so can compare values to check for the lowest value.
       lst.append(int(shoe.quantity))

    for shoe in collection:
        if f"{max(lst)}" == shoe.quantity:
            print(f"{shoe.product} is for sale!!!")
            break

while True:
    #creating a menu for the user.
    output = '-----------------------Inventory--------------------- \n'
    output += '1 - to capture a shoe \n'
    output += '2 - to view stock \n'
    output += '3 - to re-stock on the lowest quantity \n'
    output += '4 - to search for a shoe\n'
    output += '5 - to calculate the value of each item \n'
    output += '6 - to find the shoe with the highest quantity \n'
    output += '7 - to quit'
    
    print(output)

    #reading the shoe data.
    read_shoes_data()
    
    #checking user input.
    try:
        user_input = int(input('Enter selection: '))
    except Exception:
        print('Invalid Entry, please Enter a number')
        continue
    
    #checking if user entered a valid option.

    if user_input < 1 or user_input > 7:
        print('Invalid Entry, Enter a number between 1-7')
        continue

    elif user_input == 1:
        capture_shoes()
        continue

    elif user_input == 2:
        view_all()
        continue

    elif user_input == 3:
        re_stock()
        continue

    elif user_input == 4:
        
        shoe_search()
        continue

    elif user_input == 5:
        value_per_item()
        continue

    elif user_input == 6:
        highest_qty()
        continue

    elif user_input == 7:
        break
    

