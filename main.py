import os
from tabulate import tabulate
from customer_transactions import Customer, Transactions
from validators import (
    login,
    validate_name,
    validate_contact,
    validate_password,
    validate_pin,
    generate_accnum,
)


def main():
    MAX_ATTEMPTS = 5
    attempts = 0

    # Display welcome message
    print()
    effect1 = [["🌎 Welcome to the Global Internet Banking Services"]]
    print(tabulate(effect1, tablefmt="simple"))
    print()
    # Display menu options
    effect2 = [["Press 1", "Account Login"], ["Press 2", "Create A New Account"]]
    print(tabulate(effect2, tablefmt="grid"))

    # Main Logic for user selection ( Account Login or Create A New Account)

    while attempts < MAX_ATTEMPTS:
        try:
            user_choice = int(input("\nSelect: "))
            os.system("clear")

            if user_choice == 1:
                handle_login()
                break

            elif user_choice == 2:
                create_new_account()
                break

            else:
                print("Invalid input! Please choose 1 or 2.")
                attempts += 1

        except ValueError:
            print("Invalid input! Please enter a number.")
            attempts += 1
   

def handle_login():
    attempts = 0
    while attempts < 5:
        try:
            user_accnum = input("\nAccount Num: ")
            user_password = input("Password: ")
            os.system("clear")

            name, acc_num, pin = login(user_accnum, user_password)
            customer_balance = Transactions(
                name, acc_num, pin
            )  # To Get account balance
            display_balance(name, customer_balance.balance)

            while transaction_flow(name, acc_num, pin):
                continue
            break  # Successfully logged out, exiting the loop.

        except ValueError:
            print("\nEither Account Number or Password is Incorrect. Please try again.")
            attempts += 1
            if attempts >= 5:
                print("Maximum attempts reached.")
                break


def display_balance(name, balance):
    effect3 = [
        [f"Welcome  {name}"],
        [f"Account Balance: ₹{balance:,}"],
    ]
    print(tabulate(effect3, tablefmt="rst"))


def transaction_flow(name, accnum, pin):
    transaction_choice = 0
    while transaction_choice < 5:
        print()
        effect4 = [
            ["Press 1", "Deposit Money"],
            ["Press 2", "Withdraw Money"],
            ["Press 3", "Account Statement"],
            ["Press 4", "Logout"],
        ]
        print(tabulate(effect4, tablefmt="grid"))
        try:
            action_choice = int(input("\nSelect: "))
            os.system("clear")

            if action_choice == 1:
                deposit_money(name, accnum, pin)
                return True
            elif action_choice == 2:
                withdraw_money(name, accnum, pin)
                return True

            elif action_choice == 3:
                view_account_statement(name, accnum, pin)
                return True

            elif action_choice == 4:
                print("\nLogged out\n")
                return False
            else:
                print("Invalid input! Please choose a valid action.")
                transaction_choice += 1

        except ValueError:
            print("Invalid input! Please enter a number.")
            transaction_choice += 1
    print("Maximum attempts exceeded.")


def deposit_money(name, accnum, pin):
    action = Transactions(name, accnum, pin)
    deposit_attempts = 0
    amount = int(input("\nAmount to Deposit: ₹"))

    while deposit_attempts < 3:
        pin_num = input("\nPlease Enter Your Transaction Pin: ")
        new_balance = action.deposit(amount, pin_num)

        if new_balance:
            effect6 = [
                [f"Amount ₹{amount:,} is successfully deposited."],
                [f"Account Balance: ₹{new_balance:,}"],
            ]
            print(tabulate(effect6, tablefmt="rst"))
            action.write_record()
            return
        else:
            deposit_attempts += 1

    print("Maximum Deposit attempts exceeded.")


def withdraw_money(name, accnum, pin):
    action = Transactions(name, accnum, pin)
    withdrawal_attempts = 0

    while withdrawal_attempts < 3:
        amount = int(input("\nAmount to Withdraw: ₹"))
        pin_attempts = 0

        while pin_attempts < 3:
            pin_num = input("\nPlease Enter Your Transaction Pin: ")
            new_balance = action.withdraw(amount, pin_num)

            if new_balance == "Incorrect Pin!":
                pin_attempts += 1
                withdrawal_attempts += 1
                continue
            elif new_balance == "Insufficient!":
                withdrawal_attempts += 1
                break

            else:
                effect7 = [
                    [f"Amount ₹{amount:,} is successfully debited."],
                    [f"Account Balance: ₹{new_balance:,}"],
                ]
                print(tabulate(effect7, tablefmt="rst"))
                action.write_record()
                return

    print("Maximum withdrawal attempts exceeded.")


def view_account_statement(name, accnum, pin):
    action = Transactions(name, accnum, pin)
    action.append_transactions()
    action.generate_statement()


def create_new_account():
    # Receiving Data from a new customer.
    print("\nKindly Enter your Details\n")

    name = validate_name()
    contact = validate_contact()
    accnum = generate_accnum()
    password = validate_password()
    pin = validate_pin()

    # Store new customer data
    new_account = Customer(name, contact, accnum, password, pin)
    new_account.store_data1()
    new_account.store_data2()

    effect5 = [[f"Please Note Your Account Number: {accnum}"]]
    print(tabulate(effect5, tablefmt="grid"))


if __name__ == "__main__":
    main()
