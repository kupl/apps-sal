n=int(input())
for i in range(n):
    k=int(input())
    while 1:
        if k%10==0:
            k=int(k/10)
        else:
            break
    k=str(k)
    print(k[::-1])
