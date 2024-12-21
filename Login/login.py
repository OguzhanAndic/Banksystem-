import mariadb
#import asyncio 


def make_acount():
    while True:
        firstname = input(f'First name: ')
        lastname = input(f'Last name: ')
        if any(char.isdigit() for char in firstname) or any (char.isdigit() for char in lastname):
            print('Names cant have nummbers in them, try again')
        else:
            break
    while True:
        password = input(f'Password: ')
        if not password.isdigit():
            print('password must be digits, try again')
        else: 
            break
    print(f"\n Account has been sucessfully made \n Firstname: {firstname} \n Lastname: {lastname} \n Password: {password}")

