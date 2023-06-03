import random


print('welcome to passwords generator!')
len_password = int(input('what len of password do you want: '))

alphobit = 'qwertyuiopasdfghjklzxcvbnm1234567890'
symbols = r'!?|/\@#$%^&*()-+'

print('do you want that your password include special symbols( ! ? | etc.)')
flag = input('yes or no? ')

password = ''

while flag not in ['yes', 'no', 'Yes', 'No']:
    flag = input('invalid answer!! yes or no? ')

for i in range(len_password):
    if flag in ('yes', 'Yes'):
        password += random.choice(alphobit+symbols)
    else:
        password += random.choice(alphobit)
        
print('This is your new password: ', password)
print('Good luck!!!')
