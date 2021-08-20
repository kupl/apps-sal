for _ in range(int(input())):
    (chef, cook, k) = map(int, input().split())
    ans = (chef + cook) // k
    if ans % 2 == 0:
        print('CHEF')
    else:
        print('COOK')
