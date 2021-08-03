T = int(input())
ans = []

for _ in range(T):
    N = input().strip()

    count = 0
    for i in N:
        if(i != '4' and i != '7'):
            count += 1
    ans.append(count)

for i in ans:
    print(i)
