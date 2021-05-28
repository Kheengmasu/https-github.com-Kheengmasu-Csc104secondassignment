print('here are the available bank ussd codes: \n1. Standard chartered: *977#')
ussd = input('please type in your banks USSD code: ')
def menu():
    option = int(input('1. Check your bal\n2. Transfers\n3. Airtime\n4.Transaction History\n\nPlease select an option: '))
    if(option == 1):
        print('Your acc bal is 284736465 naira')
        main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
        if(main == 1):
            menu()
        elif(main == 2):
            exit()
        else:
            print('input error!')
    elif(option == 2):
        num = input('Enter the Acc number you want to tranfer the money to: ')
        amount = input('Enter amount: ')
        pin = input('Enter six digits pin: ')
        compilation = 'Do you want to send'+amount+'to this account number: '+ num+'?\n1. Yes\n2. No\n'
        assure = input(compilation)
        if(assure == '1'):
            print('Transaction successful')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')            
        elif(assure == '2'):
            print('transanction cancelled')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')
    elif(option == 3):
        choice = int(input('1. for self\n2. for others\n'))
        if(choice == 1):
            amount = (input('Enter amount: '))
            print('Transaction successful')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')
        elif(choice == 2):
            amount=(input('Enter amount: '))
            number = input('Enter the phone number you want to buy airtime for: ')
            compilation = 'Do you want to buy '+ amount+ ' naira worth of airtime for '+ number+'?: \n1. Yes\n2. No\n'
            assure = int(input(compilation))
            if(assure == 1):
                print('Transaction successful')
                main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
                if(main == 1):
                    menu()
                elif(main == 2):
                    exit()
                else:
                    print('input error!')
            elif(assure == 2):
                print('Transaction cancelled')
                main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
                if(main == 1):
                    menu()
                elif(main == 2):
                    exit()
                else:
                    print('input error!')
            else:
                print('invalid input')
    elif(option == 4):
        print('An sms would be sent to you shortly')
if(ussd == '*977#'):
    menu()
else:
    print('wrong input')