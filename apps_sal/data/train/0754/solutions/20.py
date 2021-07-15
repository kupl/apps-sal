# cook your dish here
n=int(input())
ls=[]
for _ in range(n):
    ls.append(int(input()))
for ele in ls:
    ele=str(ele)
    ele=list(ele)
    flag=0
    for i in ele:
        if(int(i)%2==0):
            print("1")
            flag=1
            break
    if(flag==0):
        print("0")

