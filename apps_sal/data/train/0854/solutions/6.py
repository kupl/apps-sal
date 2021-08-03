for _ in range(int(input())):
    a = input()
    l = list(map(int, input().split()))
    c = 0
    for i in l:
        if l.count(i) > 1:
            c = 1
            break
    if c == 0:
        print("prekrasnyy")
    else:
        print("ne krasivo")
