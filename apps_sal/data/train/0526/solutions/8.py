# cook your dish here
for _ in range(int(input())):
    s=input()
    size1=8*len(s)
    size2=8
    i=1
    while i<len(s):
        if s[i]==s[i-1]:
            while s[i]==s[i-1]:
                i+=1
                if i>=len(s):
                    break
            size2+=32
        else:
            size2+=8
            i+=1
    print(size1-size2)
