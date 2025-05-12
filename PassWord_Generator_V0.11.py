import string
from random import randint
import math

def algorith():
    pi = math.pi
    random_numbers = (randint(1, 4) * pi / math.factorial(randint(1, 4))) * randint(1, 10)
    return int(round(random_numbers, 0))


def random_key():
    number_count = int(input("How many characters are your password?: "))
    key_log = []
    for i in range(0, number_count):
        key = algorith()
        while key in key_log:
            key = algorith()
        key_log.append(key)
    return key_log


def load_character():
    letters_upper = []
    letters_lower = []
    symbols = []
    numbers_ = []

    for i in string.ascii_uppercase:
        letters_upper.append(i)

    for i in string.ascii_lowercase:
        letters_lower.append(i)

    for i in string.punctuation:
        symbols.append(i)

    for i in string.digits:
        numbers_.append(i)

    return letters_upper, letters_lower, symbols, numbers_


def password_generator(var1, var2, var3, var4, var5):
    password = []
    upper_letters = int(len(var1))
    lower_letters = int(len(var2))
    symbol_letters = int(len(var3))
    number_letters = int(len(var4))
    key_length = int(len(var5))

    for i in range(0, key_length - 1):
        if var5[i] in range(64, 79) or var5[i] in range(32, 47):
            password.append(var4[randint(0, number_letters - 1)])

        if var5[i] in range(96, 111) or var5[i] in range(48, 63):
            password.append(var1[randint(0, upper_letters - 1)])

        if var5[i] in range(0, 15) or var5[i] in range(80, 95):
            password.append(var2[randint(0, lower_letters - 1)])

        if var5[i] in range(16, 31) or var5[i] in range(112, 127):
            password.append(var3[randint(0, symbol_letters - 1)])
    return password


def main():
    letters_uppercase, letters_lowercase, symbols_, numbers_ = load_character()
    key = random_key()
    password = password_generator(letters_uppercase, letters_lowercase, symbols_, numbers_, key)
    password_generated = "".join(password)


    print(f"These are the uppercase letters: {letters_uppercase}\n"
          f"These are the lowercase letters: {letters_lowercase}\n"
          f"These are the symbols: {symbols_}\n"
          f"And these are the numbers: {numbers_} and Key: {key}\n"
          f"Password: {password_generated}")


if __name__ == "__main__":
    main()