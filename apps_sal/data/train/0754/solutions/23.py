t=int(input())
for _ in range(0,t):
    n=int(input().strip())
    ok=False
    while n>0:
        rem= n % 10
        #print(rem)
        if rem % 2==0:
            ok=True
            break
        else:
            n=n//10
    if ok ==  True:
        print("1")
    else:
        print("0")
