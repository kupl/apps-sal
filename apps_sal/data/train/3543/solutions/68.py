def increment_string(s):
    num = ""
    zerosFound = False
    zeros = 0
    result = ""
    for x, i in enumerate(s):
        if(i.isdigit()):
            if(int(i) > 0):
                zerosFound = True
            if(i == "0" and not zerosFound):
                zeros += 1
            num += i
        if(not i.isdigit() and num is not ''):
            num = ''
            zeros = 0
            zerosFound = False
    if(num is not '' and int(num) > 0):
        print("J")
        result = s.replace(num, '')
        if(len(str(int(num) + 1)) is not len(str(int(num)))):
            zeros -= 1
        result += str("0" * zeros) + str(int(num) + 1)
    else:
        result = s + "1" if s[-1:] is not "0" else s[:-1] + "1"
    return result
