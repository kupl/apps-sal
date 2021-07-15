# cook your dish here
t=int(input())
for i in range(0,t):
    my_ip = int(input().strip())
    for xyz in range(my_ip+1):
        for abc in range(0,xyz+1):
            if abc == xyz:
                print(xyz,end="")
            else:
                print('*',end="")

        print()
