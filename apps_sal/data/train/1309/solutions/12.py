# cook your dish here
t=int(input())
for i in range(0,t):
    my_inp = int(input().strip())
    for abc in range(my_inp):
        for xyz in range(1,abc+1):
            print('*',end="")
        for xyz in range(my_inp-abc):
            print(my_inp-abc-xyz,end="")

        print()
