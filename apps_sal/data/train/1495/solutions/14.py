def check1(array):
    last = [0 for i in range(10)]
    last[8] += min(array[8], array[1])
    last[1] = min(array[8], array[1])
    array[1] -= min(array[8], array[1])
    last[7] += min(array[7], array[2])
    last[2] += min(array[7], array[2])
    array[2] -= min(array[7], array[2])
    while array[5] != 0 and array[4] != 0:
        last[5] += 1
        last[4] += 1
        array[5] -= 1
        array[4] -= 1
    while array[5] != 0 and array[1] != 0:
        last[5] += 1
        last[1] += 1
        array[5] -= 1
        array[1] -= 1
    last[4] += min(array[4], array[2])
    last[2] += min(array[4], array[2])
    array[2] -= min(array[4], array[2])
    last[2] += min(array[1], array[2])
    last[1] += min(array[1], array[2])
    temp = array[1]
    array[1] -= min(array[1], array[2])
    array[2] -= min(temp, array[2])
    for i in range(10):
        if i % 3 == 0:
            last[i] += array[i]
        else:
            last[i] += (array[i] - array[i] % 3)
    ans = [str(i) * last[i] for i in range(10)]
    return int(''.join(ans[::-1]))


def check2(array):
    last = [0 for i in range(10)]
    for i in range(10):
        if i % 3 == 0:
            last[i] += array[i]
        else:
            last[i] += (array[i] - array[i] % 3)
            array[i] -= last[i]
    last[8] += min(array[8], array[1])
    last[1] += min(array[8], array[1])
    array[1] -= min(array[8], array[1])
    last[7] += min(array[7], array[2])
    last[2] += min(array[7], array[2])
    array[2] -= min(array[7], array[2])
    while array[5] != 0 and array[4] != 0:
        last[5] += 1
        last[4] += 1
        array[5] -= 1
        array[4] -= 1
    while array[5] != 0 and array[1] != 0:
        last[5] += 1
        last[1] += 1
        array[5] -= 1
        array[1] -= 1
    last[4] += min(array[4], array[2])
    last[2] += min(array[4], array[2])
    array[2] -= min(array[4], array[2])
    last[2] += min(array[1], array[2])
    last[1] += min(array[1], array[2])
    temp = array[1]
    array[1] -= min(array[1], array[2])
    array[2] -= min(temp, array[2])
    ans = [str(i) * last[i] for i in range(10)]
    return int(''.join(ans[::-1]))


T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    array = [0 for i in range(10)]
    arr = list(map(int, input().strip().split()))
    for j in arr:
        array[j] += 1
    if array[0] == 0:
        print(-1)
    else:
        array1 = array[:]
        a = check1(array)
        b = check2(array1)
        print(max(a, b))
