from abc import ABC, abstractmethod
from datetime import datetime

class Bill(ABC):
    def __init__(self, user, amount, due_date):
        # Initialize attributes
        self.user = user
        self.amount = amount
        self.due_date = due_date

    # Setter for due_date
    def set_due_date(self, due_date):
        self.due_date = due_date

    # Getter for due_date
    def get_due_date(self):
        return self.due_date

    # Method to calculate the number of days overdue
    def calculate_days_overdue(self):
        current_date = datetime.now().date()
        return (current_date - self.due_date).days

    # Abstract method to calculate the late fee
    @abstractmethod
    def calculate_late_fee(self):
        pass

    # Static method to prompt for late fee
    @staticmethod
    def prompt_for_late_fee(bill):
        late_fee = bill.calculate_late_fee()
        days_overdue = bill.calculate_days_overdue()

        print(f"This bill is {days_overdue} days overdue.")
        print(f"Late fee for this bill is: ${late_fee:.2f}")
