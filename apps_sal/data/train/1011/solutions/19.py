T = int(input())
for i in range(T):
    N, K = list(map(int, input().split(" ")))
    msg = input()
    lower = 0
    upper = 0
    for s in msg:
        if ord(s) in range(65, 91):
            upper += 1
        elif ord(s) in range(97, 123):
            lower += 1
    if K > N:
        print("both")
    elif lower == upper:
        if K >= lower:
            print("both")
        else:
            print("none")
    elif lower < upper:
        if K < lower:
            print("none")
        elif K >= upper:
            print("both")
        else:
            print("brother")
    elif upper < lower:
        if K < upper:
            print("none")
        elif K >= lower:
            print("both")
        else:
            print("chef")
