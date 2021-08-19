
T = int(input())
for _ in range(T):
    N = int(input())
    V = list(str(N))
    # fa=ckt(N)
    ans = ""
    n = len(V)
    for i in range(n):
        if (i != (n - 1) and V[i] > V[i + 1]):
            ans = list(ans + str(int(V[i]) - 1) + ("9") * (n - i - 1))
            for j in range(i - 1, -1, -1):
                if (ans[j] > ans[j + 1]):
                    ans[j + 1] = "9"
                    ans[j] = str(int(ans[j]) - 1)
                else:
                    break
            break
        else:
            ans = ans + V[i]

    ans1 = ""
    for i in ans:
        ans1 = ans1 + i

    print(int(ans1))
