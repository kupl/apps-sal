def is_xor_greater(a, n):
    if a ^ n > n:
        return True
    else:
        return False


def get_don(n):
    i = 1
    while True:
        if 2 ** i >= n:
            break
        else:
            i += 1
    return 2 ** i


for t in range(int(input())):
    n = int(input().strip())
    print(get_don(n))
