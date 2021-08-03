for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    r = 0
    for i in seq:
        if seq.count(i) > 1:
            r += 1
    if r == 0:
        print("prekrasnyy")
    else:
        print("ne krasivo")
