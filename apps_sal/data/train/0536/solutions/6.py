for i in range(int(input())):
    k, w = map(int, input().split())
    if k > w:
        print(0)
    else:
        print(w // k)
