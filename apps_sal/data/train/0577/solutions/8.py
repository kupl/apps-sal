# cook your code here
alf = input()

n = int(input())
for _ in range(n):
    yes = 1
    x = input()
    for c in x:
        if(alf.find(c) == -1):
            yes = 0
            break
    if yes:
        print("Yes")
    else:
        print("No")
