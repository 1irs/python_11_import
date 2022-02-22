import string
import getpass

print('непечатные символы', string.whitespace)

password = getpass.getpass(prompt='Введите пароль: ')

print('Вы ввели: ', password)

at_least_one_punct = False
punct = ".,!-*"
for l in password:
    if l in string.punctuation:
        at_least_one_punct = True
        break

if at_least_one_punct:
    print(password, 'хороший пароль')
else:
    print(password, 'плохой пароль')
