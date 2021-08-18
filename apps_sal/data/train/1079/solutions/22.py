
T = int(input())
for tc in range(T):
    num = int(input())
    count = 0
    while num:
        rem = num % 10
        if rem == 4:
            count += 1
        num = num // 10
    print(count)
