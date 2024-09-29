class User:
    def __init__(self, name, eyc=0, address='', email='', aadhar_no=0, no_of_units=0.0):
        # Initialize attributes
        self.name = name
        self.eyc = eyc
        self.address = address
        self.email = email
        self.aadhar_no = aadhar_no
        self.no_of_units = no_of_units

    # Setters
    def set_name(self, name):
        self.name = name

    def set_eyc(self, eyc):
        self.eyc = eyc

    def set_address(self, address):
        self.address = address

    def set_email(self, email):
        self.email = email

    def set_no_of_units(self, no_of_units):
        self.no_of_units = no_of_units

    def set_aadhar_no(self, aadhar_no):
        self.aadhar_no = aadhar_no

    # Getters
    def get_name(self):
        return self.name

    def get_eyc(self):
        return self.eyc

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def get_aadhar_no(self):
        return self.aadhar_no

    def get_no_of_units(self):
        return self.no_of_units

    # Method to calculate the billed amount for domestic usage
    def billed_amount_domestic(self):
        num = self.no_of_units

        if num <= 150:
            money = num * 2.75
        elif 150 < num < 400:
            money = num * 4.80
        else:
            money = num * 5.20

        print(money)
        return money

    # Placeholder for total units (can be implemented if needed)
    def total_units(self):
        return 0

    # String representation of the user details
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"EYC Number: {self.eyc}\n"
                f"Address: {self.address}\n"
                f"Email: {self.email}\n"
                f"Aadhar Number: {self.aadhar_no}\n"
                f"No. of Units: {self.no_of_units}")
