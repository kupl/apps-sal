for t in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    up = 0
    lo = 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            lo += 1
    if k >= len(s) or (k >= up and k >= lo):
        print("both")
    else:
        if lo > k and up > k:
            print("none")
        else:
            if k >= lo:
                print("brother")
            elif k >= up:
                print("chef")
