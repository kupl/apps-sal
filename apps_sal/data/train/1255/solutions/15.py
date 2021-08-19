# cook your dish here
t = int(input())
while t > 0:
    l = list(input().split())
    a = int(l[1])
    s = list(l[0])
    o = ""
    for i in range(97, 123):
        if(chr(i) in s):
            if(a > 0):
                o += chr(i)
                a -= 1
        else:
            o += chr(i)
    if(len(s) <= len(o)):
        print("".join(o[0:len(s)]))
    else:
        print("NOPE")
    t -= 1
