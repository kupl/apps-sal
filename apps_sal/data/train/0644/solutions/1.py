t = input()
for i in range(int(t)):
    n = int(input())
    l = list(map(int, input().split()))
    if(sum(l) % n == 0):
        print("Yes")
    else:
        print("No")
