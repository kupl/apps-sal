from sys import stdin
for _ in range(int(stdin.readline())):
    (m, n) = list(map(int, stdin.readline().split()))
    final = []
    arr = []
    val = 0
    extra = 0
    for j in range(m):
        ans = list(map(str, stdin.readline().split()))
        if ans.count('N') == n:
            val += 1
        else:
            if val % 2 == 0:
                arr.append(ans)
                extra += val
            else:
                arr.append(['N'] * n)
                arr.append(ans)
                extra += val - 1
            val = 0
    for j in range(len(arr)):
        ans = arr[j]
        start = -1
        for i in range(n):
            if ans[i] == 'P':
                start = i
                break
        if start != -1:
            for i in range(n - 1, -1, -1):
                if ans[i] == 'P':
                    end = i
                    break
        if start != -1:
            if len(final) == 0:
                final.append([start, end])
            else:
                if j % 2 == 0:
                    if final[-1][0] > start:
                        final[-1][0] = start
                    else:
                        start = final[-1][0]
                elif final[-1][1] < end:
                    final[-1][1] = end
                else:
                    end = final[-1][1]
                final.append([start, end])
        elif len(final) != 0:
            (start, end) = (0, n - 1)
            if j % 2 == 0:
                if final[-1][0] > start:
                    final[-1][0] = start
                else:
                    start = final[-1][0]
            elif final[-1][1] < end:
                final[-1][1] = end
            else:
                end = final[-1][1]
            final.append([start, end])
    if len(final) == 0:
        print(0)
    else:
        count = 0
        for ele in final:
            count += ele[1] - ele[0] + 1
        print(count - 1 + extra)
