def palindrome(num):
    if type(num) is not int or num < 0:
        return "Not valid"
    if num < 10:
        return 0
    
    counter = 0
    num = str(num)
    for i in range(0,len(num)-1):
        for r in range(i + 2, len(num)+1):
            if num[i:r] == num[i:r][::-1]:
                counter += 1    
    return counter
