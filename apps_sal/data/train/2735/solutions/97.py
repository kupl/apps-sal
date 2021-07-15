def jumping_number(n):
    s = str(n)
    l = []
    for i in range(len(s)):
        if i < len(s)-1:
            l.append(abs(int(s[i+1])-int(s[i])))
    return 'Jumping!!' if l == [] or n =='' or sum(l) == len(s)-1 else 'Not!!'

