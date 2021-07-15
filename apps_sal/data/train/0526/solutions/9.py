# cook your dish here
n = int(input())
for i in range(n):
    s = str(input())
    o_l = len(s)*8
    n_l = 0
    t = 0
    for i in range(len(s)-1):
        if s[i] ==s[i+1]:
            t+=1
        else:
            if(t>=1):
                n_l += 32+8
            else:
                n_l += 8
            t = 0
    if(t>=1):
        n_l += 32+8
    else:
        n_l += 8
    print(o_l-n_l)

