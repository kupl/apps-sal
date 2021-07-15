# cook your dish here
def compress(a):
    prev = None
    prev_c = 1
    ans_s=""
    k=0
    for x in a:
        if prev == x:
            prev_c+=1
        else:
            if prev!=None:
                if prev_c!=1:
                    ans_s = ans_s + str(prev) + str(prev_c)
                    k+=40
                else:
                    ans_s = ans_s + str(prev)
                    k+=8
            prev_c=1
            prev =x
    if prev_c!=1:
        ans_s = ans_s + str(prev) + str(prev_c)
        k+=40
    else:
        ans_s = ans_s + str(prev)
        k+=8
    #print(ans_s)
    return k
t=int(input())
while(t):
    t=t-1
    a=input()
    ans = compress(a)
    size = 8*len(a)
    print( size - ans )
