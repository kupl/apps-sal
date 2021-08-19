n = int(input())


def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def digit_count(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


x_count = 0
x_list = []
for x in range(n - 9 * digit_count(n), n + 1):
    if x + digit_sum(x) == n:
        x_list.append(x)
        x_count += 1
print(x_count)
for x in x_list:
    print(x)
