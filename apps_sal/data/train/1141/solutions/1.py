# cook your dish here
try:
    t, s = input().split()
    for i in range(int(t)):
        s1 = eval(input())
        s1 = s1.replace("_", " ")

        aa = ""
        for i in s1:
            if(i.isalpha() == True):
                if(i.isupper() == True):
                    i = i.lower()
                    g = ord(i) % 97
                    ss1 = s[g].upper()
                    aa += ss1
                else:

                    g = ord(i) % 97
                    aa += s[g]
            else:
                aa += i
        print(aa)
except:
    pass
