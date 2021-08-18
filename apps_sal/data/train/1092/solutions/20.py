for _ in range(int(input())):
    n, k, e, m = list(map(int, input().split()))
    all_marks = []
    for i in range(n - 1):
        marks = sum(list(map(int, input().split())))
        all_marks.append(marks)

    ser = list(map(int, input().split()))

    all_marks = sorted(all_marks)

    q = all_marks[n - k - 1:]

    ser_req = min(q) - sum(ser) + 1

    if ser_req > m:
        print("Impossible")
    else:
        if ser_req > 0:
            print(ser_req)
        else:
            print(0)
