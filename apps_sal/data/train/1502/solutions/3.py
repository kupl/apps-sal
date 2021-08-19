# cook your dish here
T = int(input())
for i in range(T):
    S = input()
    n = int(input())
    arr = [str(j) for j in input().split()][:n]
    if(len(set(S) - set(arr)) == 1):
        print(1)
    else:
        print(0)
