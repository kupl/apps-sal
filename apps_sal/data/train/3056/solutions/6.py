def palindrome(num,s):
    if type(num) is not int or type(s) is not int or num <0 or s<0:
        return "Not valid"
    result =[]
    while s:
        if is_pal(num):
            result.append(num)
            s-=1
            num +=1
        else:
            num += 1
    return result
    
    
def is_pal(n):
    return n >10 and n == int(str(n)[::-1])
