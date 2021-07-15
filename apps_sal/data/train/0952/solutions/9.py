for _ in range(int(input())):
    s=input()
    sm=0
    for i in range(len(s)):
        if s[i]!='a' and s[i]!="e" and s[i]!="i" and s[i]!="o" and s[i]!="u":
            if ord(s[i])-96<=3:
                sm+=abs(ord(s[i])-97)
            elif ord(s[i])-96<=7 and ord(s[i])-96>3:
                sm+=abs(ord(s[i])-ord("e"))
            elif ord(s[i])-96<=12 and ord(s[i])-96>7:
                sm+=abs(ord(s[i])-ord('i'))
            elif ord(s[i])-96<=18 and ord(s[i])-96>12:
                sm+=abs(ord(s[i])-ord('o'))
            else:
                sm+=abs(ord(s[i])-ord("u"))
    print(sm)            
