
Balance=0
def check_Balance():
    print("Available Balance:",Balance)

def deposit():
    global Balance
    amt=int(input("Enter Deposit Amount:"))
    Balance +=amt
    print("Amount Deposit Successfully!")

def withdraw():
    global Balance
    amt=int(input("Enter Withdraw Amount:"))
    if Balance>=amt:
        Balance -=amt
        print("Amount Withdraw Successfully!")
    else:
        print("Insufficient Balance!")
while True:
    print("\n============ ATM MENU ============")
    print("1.check Balance")
    print("2.Deposit ")
    print("3.Withdrawl")

    choice=int (input("Enter the choice:"))

    if choice==1:
        check_Balance()
        
    elif choice ==2:
         deposit()

    elif choice==3:
        withdraw()

    elif choice==4:
        print("Thank YoU!")
        break

    else:
        print("Invalid choice!")




