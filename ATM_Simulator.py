import time
print("======================================================")
print("PLEASE ENTER YOUR CARD")
print("======================================================")
time.sleep(3)

password = 1234
pin = int(input("Enter your ATM Pin : "))
balance = 10000

if pin == password:
    while True:
        print("======================================================")
        
        print("""
            1 == Check Balance
            2 == Withdrawl Balance
            3 == Diposite Balance
            4 == Exit
            """)
        print("======================================================")
        try:
            option = int(input("Please Enter Your Choise(1/2/3/4): "))
            print("======================================================")
        except:
            print("Invalide Entry!!! Please try again ")
        if option == 1:
            print(f"Your account balance is {balance}")
            print("======================================================")
        
        elif option == 2:
            withdrawl_balance = int(input("Enter the withdrawl balance : "))
            print("======================================================")
            balance = balance - withdrawl_balance
            print(f"Rs. {withdrawl_balance} is debitated from your account")
            print("======================================================")
            print(f"Now your balance is {balance}")
            print("======================================================")
            
        elif option == 3:
            diposite_balance = int(input("Enter your deposite balance : "))
            print("======================================================")
            balance = balance + diposite_balance
            print(f"Rs. {diposite_balance} is credited to your account")
            print("======================================================")
            print(f"Now your balance is : {balance}")
            print("======================================================")
            
        elif option == 4:
            break
        else:
            print("Invalide input!!! Please try again")
else:
    print("Wrong pin !!! please enter again")
    