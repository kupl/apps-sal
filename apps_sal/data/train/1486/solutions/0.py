for j in range(int(input())):
    input()
    a = list(map(int, input().split()))
    marks = 0
    backlok = 0
    top_marks = max(a)
    topper = []
    for i in range(len(a)):
        if a[i] >= 31:
            marks += a[i]
        if a[i] < 31:
            backlok += 1
        if a[i] == top_marks:
            topper.append(i)
    print(backlok, '{:0.2f}'.format(marks / len(a), 2))
    topper.sort(reverse=True)
    for i in topper:
        print(i, ' ')
    for i in a:
        print(top_marks - i)
