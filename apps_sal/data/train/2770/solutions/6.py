def make_password(phrase):
    phrase = phrase.split(' ')
    password = ''
    for word in phrase:
        password += word[0]
    password = password.replace('I', '1').replace('i', '1')
    password = password.replace('O', '0').replace('o', '0')
    password = password.replace('S', '5').replace('s', '5')
    return password
