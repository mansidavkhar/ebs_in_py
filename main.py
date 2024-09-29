import json
import threading

class User:
    def __init__(self, name, EYC, address, email, aadhar_no, no_of_units, user_type):
        self.name = name
        self.EYC = EYC
        self.address = address
        self.email = email
        self.aadhar_no = aadhar_no
        self.no_of_units = no_of_units
        self.user_type = user_type
    
    def billed_amount_domestic(self):
        
        return self.no_of_units * 10 
    
    def __str__(self):
        return f"Name: {self.name}, EYC: {self.EYC}, Address: {self.address}, Units: {self.no_of_units}"
    
    def getNoOfUnits(self):
        return self.no_of_units
    
    def getEYC(self):
        return self.EYC

class ResidentialUser(User):
    #add specific methods or attributes for ResidentialUser
    pass


# Calculate total units consumed
def calculate_total_units_consumed(user_list):
    total_units_consumed = 0.0
    for user in user_list:
        total_units_consumed += user.getNoOfUnits()
    return total_units_consumed

# Calculate total bill
def calculate_total_bill(user_list):
    total_bill = 0.0
    for user in user_list:
        total_bill += user.billed_amount_domestic()
    return total_bill

# Multi-threading class to calculate total units and bills
class CalculatorThread(threading.Thread):
    def __init__(self, user_list):
        threading.Thread.__init__(self)
        self.user_list = user_list

    def run(self):
        total_units_consumed = calculate_total_units_consumed(self.user_list)
        print(f"Total units consumed by all users (Thread): {total_units_consumed}")

        total_bill = calculate_total_bill(self.user_list)
        print(f"Total bill for all users (Thread): {total_bill}")

def main():
    # Read JSON data
    with open('demo.json', 'r') as file:
        data = json.load(file)
    
    user_list = []

    for item in data:
        name = item['name']
        EYC = item['EYC']
        address = item['address']
        email = item['email']
        aadhar_no = item['aadharNo']
        no_of_units = item['noOfUnits']

        print(f"Name: {name}")
        print(f"EYC: {EYC}")
        print(f"Address: {address}")
        print(f"Email: {email}")
        print(f"Aadhar No: {aadhar_no}")
        print(f"No Of Units: {no_of_units}")

        # Create ResidentialUser object and add to list
        residential_user = ResidentialUser(name, EYC, address, email, aadhar_no, no_of_units, "Residential")
        user_list.append(residential_user)

    # Start the CalculatorThread
    calculator_thread = CalculatorThread(user_list)
    calculator_thread.start()
    calculator_thread.join()

    # Menu-driven logic
    while True:
        print("MENU:")
        print("1. User")
        print("2. Admin")
        print("3. Exit")
        choice = input("Please select an option: ")

        if choice == "1":
            print("User Menu:")
            print("1. Add a user")
            print("2. Display user information")
            print("3. Calculate bill")
            print("4. Payment")
            print("5. Update user")
            print("6. Delete user")
            choice_user = input("Enter option: ")

            if choice_user == "1":
                n = int(input("Enter number of users to add: "))
                for i in range(n):
                    name = input(f"Enter name for user {i+1}: ")
                    EYC = int(input("Enter 10-digit EYC: "))
                    if len(str(EYC)) != 10:
                        raise ValueError("Invalid EYC; must be 10 digits.")
                    
                    address = input("Enter address: ")
                    email = input("Enter email: ")
                    aadhar_no = int(input("Enter 12-digit Aadhar number: "))
                    no_of_units = float(input("Enter units consumed: "))

                    user = ResidentialUser(name, EYC, address, email, aadhar_no, no_of_units, "Residential")
                    user_list.append(user)
            elif choice_user == "2":
                for user in user_list:
                    print(user)
            elif choice_user == "3":
                for user in user_list:
                    billed_amount = user.billed_amount_domestic()
                    print("Billed amount for user",user_list.index(user),"is rupees",billed_amount)
                    # print(f"Billed amount for {user.index()}: {billed_amount}")
            elif choice_user == "5":
                update_eyc = int(input("Enter EYC number of user to update: "))
                found = False
                for user in user_list:
                    if user.getEYC() == update_eyc:
                        found = True
                        user.name = input("Enter updated name: ")
                        user.address = input("Enter updated address: ")
                        user.email = input("Enter updated email: ")
                        user.aadhar_no = int(input("Enter updated Aadhar number: "))
                        user.no_of_units = float(input("Enter updated units consumed: "))
                        print("User updated successfully.")
                if not found:
                    print(f"User with EYC {update_eyc} not found.")
            elif choice_user == "6":
                delete_eyc = int(input("Enter EYC number of user to delete: "))
                user_list = [user for user in user_list if user.getEYC() != delete_eyc]
                print(f"User with EYC {delete_eyc} deleted successfully.")

        elif choice == "2":
            print("Admin Menu:")
            print("1. View admin details")
            print("2. View all users")
            print("3. View total units consumed by all users")
            print("4. Calculate total bill for all users")
            admin_choice = input("Enter option: ")

            if admin_choice == "3":
                total_units = calculate_total_units_consumed(user_list)
                print(f"Total units consumed: {total_units}")
            elif admin_choice == "4":
                total_bill = calculate_total_bill(user_list)
                print(f"Total bill for all users: {total_bill}")

        elif choice == "3":
            break

if __name__ == '__main__':
    main()
