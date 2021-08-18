for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 0:
        answer = "YES"
        for i in range(n // 2):
            if a[i] == a[n // 2 + i]:
                if a[i] == -1:
                    a[i] = a[n // 2 + i] = 1
            else:
                if a[i] == -1:
                    a[i] = a[n // 2 + i]
                elif a[n // 2 + i] == -1:
                    a[n // 2 + i] = a[i]
                else:
                    answer = "NO"
                    break

        print(answer)
        if(answer == "YES"):
            print(" ".join(map(str, a)))
    else:
        print("NO")
