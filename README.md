# Password_Generator_V0.10
# First code to do a password generator. There is a problem, it get into a inifinite loop generating the password. Working on it.


import string
from random import randint

def symbols_string():
    symbols = []
    for i in string.punctuation:
        symbols.append(i)
    return symbols


def uppercase_letters():
    uppercase = []
    for i in string.ascii_uppercase:
        uppercase.append(i)
    return uppercase


def lowcase_letters():
    lowcase = []
    for i in string.ascii_lowercase:
        lowcase.append(i)
    return lowcase


def numbers_letters():
    numbers = []
    for i in string.digits:
        numbers.append(i)
    return numbers


def promedia(var1, var2, var3):
    prom = (int(len(var1)) + int(len(var2)) + int(len(var3)))/3
    prom = round(prom, 0)
    return prom


def algorithm(var1):
    algorithm_equation = int(round(((((randint(0, var1) * 2) + 5)/((randint(0, var1) * 3) + 2)) * 10), 0))
    return algorithm_equation


def random_numbers(var1, var2):
    letters = []
    for i in range(0, var1):
        n_random = algorithm(var2)
        while True:
            if n_random >= var2 + 1 or n_random in letters:
                while n_random in letters or n_random >= var2 + 1:
                    n_random = algorithm(var2)
            else:
                break
        letters.append(n_random)

    return letters
    

def numbers_generate(var1):
    prom = int(var1)
    #letters = []
    letters_number = int(input("How many characters does the password is?: "))
    random_numbers_create = random_numbers(letters_number, prom)
    return random_numbers_create


def password_generator(var1, var2, var3, var4, var5, var6):
    var_symbols = var1
    var_uppercase = var2
    var_lowcase = var3
    key = var4
    var_numbers = var5
    var_prom = int(var6 / 4)
    password = []
    iteractions = int(len(key))

    while True:
        for i in range(0, iteractions):
            if key[i] in range(0, var_prom):
                if key[i] > 9:
                    password.append(var_numbers[randint(0, 9)])
                else:
                    password.append(var_numbers[key[i]])
            elif key[i] in range(var_prom, var_prom * 2):
                if key[i] > 25:
                    password.append(var_uppercase[randint(0, 25)])
                else:
                    password.append(var_uppercase[key[i]])
            elif key[i] in range(var_prom * 2, var_prom * 3):
                if key[i] > 31:
                    password.append(var_symbols[randint(0, 31)])
                else:
                    password.append(var_symbols[key[i]])
            elif key[i] in range(var_prom * 3, var_prom * 4):
                if key[i] > 25:
                    password.append(var_lowcase[randint(0, 25)])
                else:
                    password.append(var_lowcase[key[i]])

        if int(len(password)) == iteractions:
            break
    return password


def main():

    symbols = symbols_string()
    uppercase = uppercase_letters()
    lowcase = lowcase_letters()
    promed = promedia(symbols, uppercase, lowcase)
    letters = numbers_generate(promed)
    numbers = numbers_letters()
    password = password_generator(symbols, uppercase, lowcase, letters, numbers, promed)
    password_string = ''.join(password)
    print(f"This is your password: {password_string}")
    input("Press any key to exit")

    #print(symbols, uppercase, lowcase, promed)
    

if __name__ == "__main__":
    main()
