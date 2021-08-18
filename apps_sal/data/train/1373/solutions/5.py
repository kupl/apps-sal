for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ans, temp = 0, 0

    if k == 2:
        l1 = [0, 0]
        for i in l:
            l1[i - 1] = 1
            temp += 1
            if l1 == [1, 1]:
                ans = max(ans, (temp - 1))
                l1 = [0, 0]
                l1[i - 1] = 1
                temp = 1

    else:
        l1 = []
        for i in range(n):
            l1.append(l[i])
            temp = 1
            for j in range(i + 1, n):
                if l[j] in l1:
                    temp += 1

                else:
                    if len(l1) == k - 1:
                        l1 = []
                        ans = max(ans, temp)
                        break

                    else:
                        l1.append(l[j])
                        temp += 1

            ans = max(ans, temp)

    print(max(ans, temp))
