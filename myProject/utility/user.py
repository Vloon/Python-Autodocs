class User:
    """A user consists of a first name, last name, user ID, and a balance amount.
    """
    def __init__(self, first_name:str, last_name:str, user_id:int, balance:float):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.balance = balance

    def full_name(self) -> str:
        """Returns the full name of the user

        Returns:
            str: the user's full name
        """
        return f"{self.first_name} {self.last_name}"

    def add(self, amount:float) -> float:
        """Adds the amount to the balance and returns the new balance

        Args:
            amount (float): The amount to add to the balance

        Returns:
            float: The new value of the balance
        """
        assert amount > 0, f"Amount should be larger than 0 but is f{amount}"
        self.balance += amount
        return self.balance


    def bill(self, amount:float) -> float:
        """Subtracts the amount from the user's balance, and returns the remaining balance

        Args:
            amount (float): amount to bill the user

        Returns:
            float: the remaining amount after billing the user
        """
        assert amount > 0, f"Amount should be larger than 0 but is f{amount}"
        self.balance -= amount
        return self.balance

    def has_debt(self) -> bool:
        """Returns whether the user has a debt

        Returns:
            bool: whether the user's balance is negative.
        """
        return self.balance < 0