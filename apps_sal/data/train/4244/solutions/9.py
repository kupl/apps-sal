from collections import Counter
def palindrome(num):
    if not isinstance(num, int) or num<0:
        return 'Not valid'
    elif num<=10:
        return False
    check=Counter(str(num))
    count=0
    for i in check:
        if check[i]%2:
            count+=1
    return True if count==0 else True if (count==1 and len(str(num))%2 ) else False
