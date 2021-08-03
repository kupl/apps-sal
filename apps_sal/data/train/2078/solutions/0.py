def main():
    n = int(input())
    a = list(map(int, (x for x in input())))
    b = list(map(int, (x for x in input())))
    x = [0] * (n - 1)
    x[0] = b[0] - a[0]
    for i in range(1, n - 1):
        x[i] = b[i] - a[i] - x[i - 1]
    if a[n - 1] + x[n - 2] != b[n - 1]:
        print(-1)
        return
    cnt = sum(map(abs, x))  # prevbug: ftl
    print(cnt)
    cnt = min(cnt, 10 ** 5)
    index = 0

    def handle_zero_nine(cur_zero):
        nonlocal cnt
        nxt = index + 1
        # cur_zero = True prevbug: preserved this line
        while True:
            if cur_zero and a[nxt + 1] != 9:
                break
            if not cur_zero and a[nxt + 1] != 0:
                break
            nxt += 1
            cur_zero = not cur_zero
        while nxt > index:
            if cnt == 0:
                break
            if cur_zero:
                print(nxt + 1, 1)
                a[nxt] += 1
                a[nxt + 1] += 1
            else:
                print(nxt + 1, -1)
                a[nxt] -= 1
                a[nxt + 1] -= 1
            nxt -= 1
            cnt -= 1
            # print(a)
            cur_zero = not cur_zero

    while cnt > 0:
        if a[index] == b[index]:
            index += 1
            continue
        elif a[index] > b[index] and a[index + 1] == 0:
            handle_zero_nine(True)
        elif a[index] < b[index] and a[index + 1] == 9:
            handle_zero_nine(False)
        elif a[index] > b[index]:
            print(index + 1, -1)
            a[index] -= 1
            a[index + 1] -= 1
            cnt -= 1
            # print(a)
        elif a[index] < b[index]:
            print(index + 1, 1)
            a[index] += 1
            a[index + 1] += 1
            cnt -= 1
            # print(a)


def __starting_point():
    main()


__starting_point()
