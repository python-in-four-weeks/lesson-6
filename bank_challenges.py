from typing import TypedDict


class AccountData(TypedDict):
    account_number: str
    customer_name: str
    balance: float


account_dataset: list[AccountData] = [
    {"account_number": "12169553", "customer_name": "Alice Smith", "balance": 50},
    {"account_number": "82309802", "customer_name": "Bob Jones", "balance": 200},
    {"account_number": "38987723", "customer_name": "Charlie Taylor", "balance": 100},
    {"account_number": "32605081", "customer_name": "David Brown", "balance": 70},
    {"account_number": "87630077", "customer_name": "Eve Williams", "balance": 20},
    {"account_number": "04985834", "customer_name": "Frank Wilson", "balance": 250},
    {"account_number": "77195058", "customer_name": "Grace Johnson", "balance": 150},
    {"account_number": "83670310", "customer_name": "Heidi Davies", "balance": 125},
    {"account_number": "40469993", "customer_name": "Ivan Patel", "balance": 175},
    {"account_number": "92174700", "customer_name": "Judy Robinson", "balance": 220},
    {"account_number": "75029429", "customer_name": "Mallory Wright", "balance": 30},
]


class BankAccount:
    def __init__(self, account_number: str, customer_name: str, balance: float):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    @classmethod
    def from_account_data(cls, account_data: AccountData):
        return cls(
            account_data["account_number"],
            account_data["customer_name"],
            account_data["balance"],
        )

    def deposit(self, amount: float) -> None:
        pass

    def withdraw(self, amount: float) -> None:
        pass


class ATM:
    def __init__(self, accounts: dict[str, BankAccount]):
        self.accounts = accounts

    @classmethod
    def from_account_dataset(cls, account_dataset: list[AccountData]):
        return cls(
            {
                account_data["account_number"]: BankAccount.from_account_data(
                    account_data
                )
                for account_data in account_dataset
            }
        )

    def process_deposit(self, account_number: str) -> None:
        pass

    def process_withdrawal(self, account_number: str) -> None:
        pass

    def serve_customer(self, account_number: str) -> None:
        print(f"Would you like to deposit or withdraw money today?")
        while True:
            print("[D] Deposit")
            print("[W] Withdraw")
            print("[X] Cancel")
            action_code = input(
                "Please enter the letter that corresponds to the action you'd like to take: "
            ).casefold()
            if action_code == "d":
                self.process_deposit(account_number)
                break
            elif action_code == "w":
                self.process_withdrawal(account_number)
                break
            elif action_code == "x":
                print("No problem. Thank you for your visit!")
                break
            else:
                print("That doesn't seem to be one of the options. Please try again.")

    def menu(self) -> None:
        account_number = input("Please enter your account number: ")
        if account_number in self.accounts:
            print(f"Welcome, {self.accounts[account_number].customer_name}.")
            self.serve_customer(account_number)
        else:
            print("That account number is not recognised.")


if __name__ == "__main__":
    # Try out your functions here
    atm = ATM.from_account_dataset(account_dataset)
    atm.menu()
