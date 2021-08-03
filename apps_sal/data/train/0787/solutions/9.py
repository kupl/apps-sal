for _ in range(int(input())):
    arr = list(input())
    n = len(arr)
    for i in reversed(range(n)):
        if arr[i] == '1':
            arr.pop()
        else:
            break
    n = len(arr)
    zero = prev = total = cnt = 0
    for i in reversed(range(n)):
        if arr[i] == '0':
            zero += 1
            continue
        if prev != zero:
            prev = zero
            cnt += 1
        total += cnt + zero
    print(total)
