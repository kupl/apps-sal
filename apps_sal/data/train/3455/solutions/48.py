def disarium_number(num):
    return 'Disarium !!' if sum((int(i) ** idx for (idx, i) in enumerate(str(num), 1))) == num else 'Not !!'
