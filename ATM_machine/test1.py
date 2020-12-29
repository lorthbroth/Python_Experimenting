# A simple ATM program with a simple 1234 pin
print('##############################################\n')
print('----------------------------------------------')
print('|                                            |')
print("|       Welcome To MonarengFX ATM            |")
print('|                                            |')
print('----------------------------------------------\n')
print('##############################################\n')

restart = ('Y')
chances = 3
balance = 2000.00
while chances >= 0:
    pin = int(input("Please Enter your four digit pin: "))
    if pin == (1234):
        print("      ****Pin approved****\n")
        while restart not in ('n', 'NO', 'no', 'N'):
            print("Please press 1 for your balance\n")
            print('please press 2 for withdrawal\n')
            print('Please press 3 to make a deposit\n')
            print('Please press 4 to return Card\n')
            option = int(input('What would you like to choose? '))
            
            if option == 1:
                print('Your balance is R',balance)
                restart = input("Would like to go back? ")
                
                if restart in ('n','NO','no','N'):
                    print('Thank you')
                    break
                
                elif option == 2:
                    option2 = ('Y')
                    withdrawal1 = float(input('How much would you like to withdraw? '))
                    if withdrawal1 in [10, 20, 50, 100, 150, 200]:
                        balance = balance - withdrawal1
                        print('\nYour balance is now: R',balance)
                        restart = input('would you like to go back?')
                        if restart in ('n','NO','no','N'):
                            print('Thank you')
                            break
                        elif withdrawal1 != [10, 20, 50, 100, 150, 200]:
                            print('invalid amount Please re-try\n')
                            restart = ('Y')
                        elif withdrawal1 == 1:
                            withdrawal1 = float(input('Please enter Desired amount: '))
                            
                    elif option == 3:
                        Deposit = float(input('How much you like to deposit? '))
                        balance = balance + Deposit
                        print('Your Balance is now R:')
                        restart = input('would you like to go back? ')
                        if restart in ('n','NO','no','N'):
                            print('Thank you')
                            break
                    
                    elif option == 4:
                        print('Please wait while you card is being returned.............\n')
                        print('Thank you for your service')
                        break
                    else:
                        print('Please enter the correct number. \n')
                        restart = ('Y')
                        
    elif pin != ('1234'):
        print('!!Incorrect PIN!!')
        chances = chances - 1
        if chances == 0:
            print('\nYou have entered your Pin wrong 3 times\n CARD BLOCKED!!!')
            break                    
                