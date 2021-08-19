def solve(n, k):
    list1 = list(range(n))
    list1_values = list(list1)
    ball = list1[k]
    counter = 0
    final_list = []
    for i in range(n):
        list1.reverse()
        final_list.append(list1.pop(0))
    position = final_list.index(ball)
    return position
