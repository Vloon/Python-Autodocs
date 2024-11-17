from utility.user import User
from utility.user_manager import UserManager
import random 

if __name__ == '__main__':
    first_names = ['Alice', 'Bob', 'Britney', 'Clarence', 'Denise']
    last_names = ['Aardvark', 'Beaver', 'Beaver', 'Cow', 'Dolphin']

    user_manager = UserManager()

    for first_name, last_name in zip(first_names, last_names):
        user = user_manager.add_new_user(first_name, last_name)
        print(f"Created user {user.full_name()} with ID {user.user_id}")

    print('')
    min_amount, max_amount = 1_000, 10_000
    for user in user_manager.users:
        amount = random.uniform(min_amount, max_amount)
        current_balance = user.add(amount)
        print(f"{user.full_name()} has a balance of ${current_balance}")

    print('')
    min_bill, max_bill = 2_000, 10_000
    for user in user_manager.users:
        amount = random.uniform(min_bill, max_bill)
        current_balance = user.bill(amount)
        print(f"{user.full_name()} now has a balance of ${current_balance}")

    print('')
    users_in_debt = user_manager.get_users_with_debt()
    for user in users_in_debt:
        print(f"{user.full_name()} has a debt of ${-1*user.balance:.2f}")

    print('')
    users_named_beaver = user_manager.get_user('Beaver')
    for user in users_named_beaver:
        print(f"User {user.full_name()} has 'Beaver' in their name!")