def xor(a, b):
    answer = 0
    if a == True:
        answer += 1
    if b == True:
        answer += 1
    if answer == 1:
        return True
    else:
        return False
