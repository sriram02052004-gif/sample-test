import calc as ca
user_data={'username':'user1',
           'acc no': '123456789',
           'pin':'1234',
           'total_bal': 10000}

def user_info():
    if user_data and user_data['username']:
        return f'hii welcome user {user_data["username"]} your account number is {user_data["acc no"]} and your total balance is {user_data["total_bal"]}'
    else:
        return False

def withdraw(withdrawal_amount):
    if withdrawal_amount > user_data['total bal']:
        return False
    else:
        amount= ca.withdraw_calc(user_data['total bal'],withdrawal_amount)
        user_data['total bal'] = amount
        return amount

def deposit(deposit_amount):
    if deposit_amount:
        amount= ca.deposit_calc(user_data['total bal'],deposit_amount)
        user_data['total bal'] = amount
        return amount

def check_balance():
    return user_data['total bal']

def main():
    print("Welcome to the ATM")
    print('='*30)

    pin = input("Enter your PIN: ")
    if pin == user_data['pin']:
        print(user_info())

        while True:
            choice = input("Choose an option:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\n")

            match choice:
                case "1":
                    amount = int(input("Enter amount to check balance: "))
                    withdraw_resp = withdraw(amount)
                    if withdraw_resp:
                        print(f'withdrawal successful, your total balance is :{withdraw_resp}')
                    else:
                        print("insufficient balance")

                case '2':
                    amount = int(input("Enter amount to deposit: "))
                    print(f'deposit successful, your total balance is :{deposit(amount)}')

                case '3':
                    print(f'Your total balance is :{check_balance()}')

                case '4':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                case _:
                    print("Invalid option. Please try again.")
    else:
        print("Incorrect PIN. enter between 1 to 4")
        return


if __name__ =="__main__":
    main()
                                
