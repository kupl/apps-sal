a=str(4)
for _ in range(int(input())):
    n=str(input())
    count=0
    for i in n:
        if i==a:
            count+=1
    print(count)
