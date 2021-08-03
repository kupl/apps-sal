# cook your dish here
def solve(a, b):
    for i in a:
        for j in b:
            if i == j:
                return 1
    return 0


t = int(input())
for _ in range(0, t):
    a = input()
    b = input()
    if(solve(a, b)):
        print("Yes")
    else:
        print("No")
