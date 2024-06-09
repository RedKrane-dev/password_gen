from random import shuffle, choices

letters = 'abcdefghijklmnopqrstuvwxyz'
letters_upp = letters.upper()
letters_list = list(letters + letters_upp)

simbols = '~!@#$%^&*()_-+={}[]|/:;<>'
simbols_list = list(simbols)

numbers = '0123456789'
numbers_list = list(numbers)

user_input_let = int(input('Сколько букв должно быть в пароле?\n'))
user_input_sim = int(input('Сколько спец символов должно быть в пароле?\n'))
user_input_num = int(input('Сколько цифр должно быть в пароле?\n'))

rand_letter = choices(letters_list, k=user_input_let)
rand_sim = choices(simbols_list, k=user_input_sim)
rand_num = choices(numbers_list, k=user_input_num)

password_list = rand_letter + rand_sim + rand_num
shuffle(password_list)

password_str = ''.join(password_list)

print(f'Ваш пароль\n{password_str}')
