try:

    x = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(sum(q) - sum(p))

except EOFError:
    pass
