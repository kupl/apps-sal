def make_upper_case(s):
    spongebob = ''
    for i in s:
        if str(i).isnumeric() == True:
            spongebob += i
        elif str(i).islower() == True:
            spongebob += str(i).upper()
        else:
            spongebob += i
    return spongebob
