t=int(input())
for _ in range(t):
    l = input().strip()
    #pal = l[::-1]
    s = 0
    #if l == pal:
     #   print(0)
    for i in range(len(l)//2):
        s = s + (abs(ord(l[i])-ord(l[len(l)-i-1])))
            #print(abs(ord(l[i])-ord(pal[i])))
    print(s)
