from utility.user import User
from typing import Callable, List

class UserManager:
    """An automatic manager for keeping track of and filtering through users. 
    """

    def __init__(self, next_id_fn:Callable[[int], int] = lambda i:i+1):
        self.current_user_id:int = 0
        self.next_id_fn = next_id_fn
        self.users:List[User] = []

    def add_new_user(self, first_name:str, last_name:str) -> User:
        """Adds a new user to the database

        Args:
            first_name (str): the user's first name
            last_name (str): the user's last name

        Returns:
            User: the new user
        """
        new_user:User = User(first_name, last_name, self.current_user_id, 0.0)
        self.users.append(new_user)
        self.current_user_id = self.next_id_fn(self.current_user_id)
        return new_user
    
    def get_user(self, get_by:str|int) -> List[User]:
        """Gets the users which have a matching `user_id`, `first_name`, `last_name` or full name

        Args:
            get_by (str | int): what to match on (`user_id`, `first_name`, `last_name` or full name)

        Returns:
            List[User]: the list of users which match the query
        """
        if type(get_by) == str:
            is_match:Callable[[User],bool] = lambda u: u.first_name == get_by or u.last_name == get_by or u.full_name() == get_by
        elif type(get_by) == int:
            is_match:Callable[[User],bool] = lambda u: u.user_id == get_by
        return list(filter(is_match, self.users))

    def get_users_with_debt(self) -> List[User]:
        """Returns the list of users with debt

        Returns:
            List[User]: The users with debt
        """
        return list(filter(lambda u: u.has_debt(), self.users))