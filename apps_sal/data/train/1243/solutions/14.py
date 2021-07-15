# cook your dish here


for _ in range(int(input())):
    n=input()
    flag=0
    for i in n:
        if i=="0" or i=='5':
            flag=1
            break
    if flag==0:
        print('0')
    else:
        print("1")
