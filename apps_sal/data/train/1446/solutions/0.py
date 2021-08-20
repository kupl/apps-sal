T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    if N == 1:
        ans.append(2)
    elif '0' not in bin(N)[2:]:
        ans.append(N // 2)
    else:
        ans.append(-1)
for i in ans:
    print(i)
