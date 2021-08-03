def check_fib(lis):
    is_fib = True

    for i in range(2, len(lis)):
        if lis[i] != lis[i - 1] + lis[i - 2]:
            is_fib = False
            break

    if is_fib:
        return True

    lis[0], lis[1] = lis[1], lis[0]

    for i in range(2, len(lis)):
        if lis[i] != lis[i - 1] + lis[i - 2]:
            return False

    return True


t = int(input())

for _ in range(t):
    s = input()

    freq_list = [s.count(x) for x in set(s)]

    if len(freq_list) < 3:
        print("Dynamic")
        continue

    freq_list.sort()

    if check_fib(freq_list):
        print("Dynamic")
    else:
        print("Not")
