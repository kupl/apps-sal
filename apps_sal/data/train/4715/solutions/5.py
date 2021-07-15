def build_palindrome(s):
    if list(s) == list(s)[::-1]:
        return s
    
    for i in range(1, len(s)):
        if s[i:] == s[i:][::-1]: #checks if element i -> end of list == element i -> end of list, in reverse ([][] calls on elements of a nexted list)
            break
    endAdd = s + s[0:i][::-1] #adds the non symetric part to the begining of the string, in reverse order
    
    for i in range(1, len(s)):
        if s[:-i] == s[:-i][::-1]: #checks if element 0 -> i == element 0 -> i, in reverse ([][] calls on elements of a nexted list)
            break    
    frontAdd = s[-i:][::-1] + s #adds the non symetric part to the begining of the string, in reverse order
    
    print(endAdd)
    print(frontAdd)
    if len(list(endAdd)) <= len(list(frontAdd)):
        #print('1') #too see which one gets printed
        return endAdd
    else:
        #print('2') #too see which one gets printed
        return frontAdd
