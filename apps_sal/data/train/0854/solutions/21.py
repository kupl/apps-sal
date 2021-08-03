for i in range(int(input())):
    val = int(input())
    data = list(map(int, input().split()))
    data1 = list(data)
    for j in data:
        if data1.pop(0) in data1:
            print("ne krasivo")
            break
        elif len(data1) == 0:
            print("prekrasnyy")
