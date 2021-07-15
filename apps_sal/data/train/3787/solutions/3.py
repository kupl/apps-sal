def obfuscate(email):
    for rep in (('.', ' [dot] '), ('@', ' [at] ')):
        email = email.replace(*rep)
    return email
