try:
    n = int(input())
    my_list = []
    for i in range(n):
        marks = list(map(int, input().split()))
        marks = sorted(marks)
        my_list.append(marks)

    unique = 0
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) == 1:
            unique += 1
        i += 1
    print(unique)
except:
    pass
