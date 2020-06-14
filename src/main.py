# Resolve the problem!!
import string
import random 
SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)


    
def generate_password():
    password=''
    letras_pass = []
    # hagamos la elección de la longitud del password
    len_password = random.randint(8,16)
    for i in range(len_password):
        sym = random.choice(SYMBOLS)
        lower = random.choice(letters_lower)
        upper=random.choice(letters_upper)
        num= str(random.randint(0,10))
        choice = random.choice(sym + lower+ upper +num)
        letras_pass.append(choice)
    password = password.join(letras_pass)

    add_upper = random.choice(list(password))
    idx_upper = password.index(add_upper)
    password = password.replace(add_upper,random.choice(letters_upper))
    add_lower =random.choice(list(password))
    idx_lower = password.index(add_lower)
    while idx_lower==idx_upper:
        add_lower = random.choice(list(password))
        idx_lower = password.index(add_lower) 
    password = password.replace(add_lower,random.choice(letters_lower))
    add_sym = random.choice(list(password))
    idx_sym= password.index(add_sym)
    while idx_sym==idx_lower or idx_sym==idx_upper:
        add_sym = random.choice(list(password))
        idx_sym= password.index(add_sym)
    password = password.replace(add_sym,random.choice(SYMBOLS))
    add_num = random.choice(list(password))  
    idx_num = password.index(add_num)
    while idx_num in (idx_lower,idx_sym,idx_upper):
        add_num = random.choice(list(password))  
        idx_num = password.index(add_num)
    password = password.replace(add_num,str(random.randint(0,10)))


    return password
    


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    print(password)
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
