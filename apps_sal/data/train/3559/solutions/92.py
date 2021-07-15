def chromosome_check(sperm):
    #Your code here
    a = "Congratulations! You're going to have a "
    if 'Y' in sperm:
        b= 'son.'
    else:
        b='daughter.'
    return f"{a}{b}"
