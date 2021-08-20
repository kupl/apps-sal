n = int(input())


def foo(n):
    if int(n) == 2:
        return str(2 ^ 3)
    return str(int(n) ^ 2)


data = list(map(foo, input().split()))
print(' '.join(data))
