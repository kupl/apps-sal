for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_a = min(a)
    min_b = min(b)
    m = min(min_a, min_b)
    da = {}
    for item in a:
        if(item in da):
            da[item] += 1
        else:
            da[item] = 1
    for item in b:
        if(item in da):
            da[item] += 1
        else:
            da[item] = 1
    # print(da)
    correct = {}
    pos = 1
    for key, value in list(da.items()):
        if(value % 2):
            pos = 0
            break
        else:
            correct[key] = value // 2
    # print(correct)
    if(pos == 0):
        print(-1)
        continue
    ref = correct.copy()
    # vector var1,var2
    # print(correct)
    var1 = []
    var2 = []
    for i in range(0, n):
        if(ref[a[i]]):
            ref[a[i]] -= 1
        else:
            var1.append(a[i])
    ref = correct.copy()
    for i in range(0, n):
        if(ref[b[i]]):
            ref[b[i]] -= 1
        else:
            var2.append(b[i])
    if(len(var1) == 0):
        print(0)
        continue
    if(len(var1) != len(var2)):
        print(-1)
        continue
    final_value = 0
    var1.sort()
    var2.sort(reverse=True)
    for i in range(0, len(var1)):
        final_value += min(2 * m, min(var1[i], var2[i]))
    print(final_value)
