def solve(str1,str2):
    a=set(str1)
    return 1 if any(str1.count(i)>1 and i not in str2 for i in a) else 2
