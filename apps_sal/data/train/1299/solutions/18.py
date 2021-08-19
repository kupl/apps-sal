for T in range(int(input())):
    n = int(input())
    a_lst = list(map(int, input().split()))
    dish_type = []
    dish_type_count = []
    for i in a_lst:
        if i not in dish_type:
            dish_type.append(i)
    dish_type.sort()
    for j in dish_type:
        dish_indices = []
        for k in range(n):
            if a_lst[k] == j:
                if k - 1 not in dish_indices:
                    dish_indices.append(k)
        dish_type_count.append(len(dish_indices))
    print(dish_type[dish_type_count.index(max(dish_type_count))])
