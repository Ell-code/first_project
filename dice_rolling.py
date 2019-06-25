from random import randint as random

print('welcome mubas')
'''
this program is called dice rolling simulator

the program will randomly pick a number from 1 - 6 and ask the user if he will
like to continue or not 

'''

while True:
    first_num = random(1, 6)
    second_num = random(1, 6)
    print(f'({first_num} , {second_num})')
    user_input = input('would you like to continue if yes type y or yes else n or no: ').upper()
    if user_input == 'Y' or user_input == 'YES':
        continue
    elif user_input == 'N' or user_input == 'NO':
        print('ok')
        break
    else:
        print('wrong input it will terminate now')
        break


print('thank for dicing')