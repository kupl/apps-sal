# cook your dish here
for i in range(int(input())):
    num=int(input())
    cnt=0
    lst=[100,50,10,5,2,1]
    for i in range(len(lst)):
        cnt+=num//lst[i]
        num=num%lst[i]
    print(cnt)
