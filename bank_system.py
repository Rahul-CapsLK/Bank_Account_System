class BankAccount:
    defaultAccNumber = 1

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber += 1

        print(f"\nAccount created for {self.name}")
        print(f"Account Number: {self.accountNumber}")
        print(f"Initial balance: {self.balance}\n")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"New Balance: {self.balance}\n")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Remaining Balance: {self.balance}\n")
        else:
            print("Not enough balance!\n")

    def getBalance(self):
        print(f"Current Balance: {self.balance}\n")


# Store all accounts
accounts = {}

while True:
    print("----- BANK MENU -----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        balance = float(input("Enter initial balance: "))
        acc = BankAccount(name, balance)
        accounts[acc.accountNumber] = acc

    elif choice in ["2", "3", "4"]:
        acc_no = int(input("Enter Account Number: "))
        
        if acc_no in accounts:
            acc = accounts[acc_no]

            if choice == "2":
                amount = float(input("Enter amount to deposit: "))
                acc.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                acc.withdraw(amount)

            elif choice == "4":
                acc.getBalance()
        else:
            print("Account not found!\n")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!\n")