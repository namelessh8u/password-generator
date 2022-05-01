import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

welcome = ['Welcome to the Password Generator!',
           'Добро пожаловать в Генератор Пароля!']
select_language = ["Choose your language:\nType 'eng' or 'ru'.",
                   "Выберите язык:\nНапишите 'eng' или 'ru'."]
instructions = [
    '''
1. If you see "y/n?", enter "y" or "n". You can also enter "yes" or "no".

2. If there is type you please type natural number than you have to enter integer number that larger zero.

Please follow these instructions.
    ''',
    '''
    1. Если вы видите "y/n?",  то введите "y" или "n". Вы также можете ввести "yes" или "no".

    2. Если вас просят ввести натуральное число, то это значит, что вы должны ввести целое число, большее нуля.

    Пожалуйста, следуйте этим инструкциям.
    '''
]
count_message = ['Enter the natural number of passwords you want to generate.',
                 'Введите натуральное число паролей, которые вы хотите сгенерировать.']
incorrect_input = ['INCORRECT INPUT',
                   'НЕВЕРНЫЙ ВВОД']
length_message = [
    '''
Enter the length of the password.
Remember that the length of the password is a natural number, and the longer it is, the safer your password is.
    ''',
    '''
Введите длину пароля.
Помните о том, что длина пароля - это натуральное число, причем чем оно больше, тем безопаснее получится ваш пароль.
    '''
]
num_message = ["Should your password include the numbers '0123456789'?\ny/n?",
               "Включать ли в ваш пароль цифры '0123456789'?\ny/n?"]
uppercase_message = ["Should your password contain the uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'?\ny/n?",
                     "Включать ли в ваш пароль прописные буквы 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'?\ny/n?"]
lowercase_message = ["Should your password include the lowercase letters 'abcdefghijklmnopqrstuvwxyz'?\ny/n?",
                     "Включать ли в ваш пароль строчные буквы 'abcdefghijklmnopqrstuvwxyz'?\ny/n?"]
punctuation_message = ["Should your password contain the symbols '!#$%&*+-=?@^_'?\ny/n?",
                       "Включать ли в ваш пароль символы '!#$%&*+-=?@^_'?\ny/n?"]
similar_message = ["Should you exclude the ambiguous characters 'il1Lo0O' from your password?\ny/n?",
                   "Исключать ли из вашего пароля неоднозначные символы 'il1Lo0O'?\ny/n?"]
error_message = [
    '''
You entered an insufficient password length
OR
You have not selected any character set
    ''',
    '''
Вы ввели недостаточную длину пароля
ИЛИ
Не выбрали ни одного набора символов
    '''
]
your_password_message = ['Your passwords:', 'Ваши пароли:']
end_message = ['Do you want to generate passwords again?\ny/n?', 'Хотите ли вы снова генерировать пароли?\ny/n?']


def set_count_of_passwords(lang):
    print(count_message[lang])
    while True:
        count = input()
        if count.isdigit() and int(count) > 0:
            return int(count)
        else:
            print(incorrect_input[lang])


def set_the_language():
    print(select_language[0], select_language[1], sep='\n')
    while True:
        language = input()
        if language.lower() == 'eng':
            return 0
        elif language.lower() == 'ru':
            return 1
        else:
            print(incorrect_input[0], incorrect_input[1], sep='\n')


def set_password_length(lang):
    print(length_message[lang])
    while True:
        length = input()
        if length.isdigit() and int(length) > 0:
            return int(length)
        else:
            print(incorrect_input[lang])


def include_num(lang):
    print(num_message[lang])
    return yes_or_no(lang)


def include_uppercase(lang):
    print(uppercase_message[lang])
    return yes_or_no(lang)


def include_lowercase(lang):
    print(lowercase_message[lang])
    return yes_or_no(lang)


def include_punctuation(lang):
    print(punctuation_message[lang])
    return yes_or_no(lang)


def include_similar(lang):
    print(similar_message[lang])
    return yes_or_no(lang)


def yes_or_no(lang):
    while True:
        answer = input().lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            return False
        else:
            print(incorrect_input[lang])


def idiot_proof():
    password_min_length = password_num + password_uppercase + password_lowercase + password_punctuation
    return password_min_length > password_length or password_min_length == 0


def generate_password():
    char = ''
    password = ''
    password_chars = []

    if password_num:
        char += digits
        password += random.choice(digits)
    if password_uppercase:
        char += uppercase_letters
        password += random.choice(uppercase_letters)
    if password_lowercase:
        char += lowercase_letters
        password += random.choice(lowercase_letters)
    if password_punctuation:
        char += punctuation
        password += random.choice(punctuation)
    if password_similar:
        for c in 'il1Lo0O':
            char.replace(c, '')
            password.replace(c, '')

    for i in range(password_length - len(password)):
        password += random.choice(char)

    password_chars += password
    random.shuffle(password_chars)
    print(*password_chars, sep='')


print(welcome[0], welcome[1], sep='\n', end='\n\n')
app_language = set_the_language()
print(instructions[app_language])

while True:
    passwords_count = set_count_of_passwords(app_language)
    password_length = set_password_length(app_language)
    password_num = include_num(app_language)
    password_uppercase = include_uppercase(app_language)
    password_lowercase = include_lowercase(app_language)
    password_punctuation = include_punctuation(app_language)
    password_similar = include_similar(app_language)

    if idiot_proof():
        print(error_message[app_language])
        continue

    print(your_password_message[app_language])
    for _ in range(passwords_count):
        generate_password()

    print(end_message[app_language])
    if yes_or_no(app_language):
        continue
    break
