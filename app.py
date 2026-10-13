# Simple ATM Program

balance = 1000.0
pin = "1234"

print("Welcome to the ATM")

attempts = 0
while attempts < 3:
    user_pin = input("Enter your PIN: ")
    if user_pin == pin:
        print("PIN accepted.")
        break
    else:
        attempts += 1
        print("Incorrect PIN. Try again.")
        if attempts == 3:
            print("Too many failed attempts. Exiting...")
            exit()

while True:
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is: ${balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount <= 0:
                print("Deposit amount must be positive.")
            else:
                balance += amount
                print(f"Deposit successful. New balance: ${balance:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == "3":
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"Withdrawal successful. New balance: ${balance:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
