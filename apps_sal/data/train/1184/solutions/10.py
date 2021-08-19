def maximizing(array):
    cpy = array[:]
    final_list = []
    for i in range(len(array)):
        new_list = [array[i]]
        for t in range(len(cpy)):
            for j in range(len(new_list)):
                if cpy[t][0] == new_list[j][0] or cpy[t][1] == new_list[j][1]:
                    break
            else:
                new_list.append(cpy[t])
        cpy.remove(array[i])
        final_list.append(new_list)
    costing = []
    for i in final_list:
        cost = 0
        count_array = []
        if len(i) < 4:
            cost -= (4 - len(i)) * 100
        for j in i:
            count_array.append(arrays.count(j))
        count_array.sort(reverse=True)
        threshold = 100
        for k in count_array:
            cost += k * threshold
            threshold -= 25
        costing.append(cost)
    return max(costing)


test_cases = int(input())
output_list = []
for _ in range(test_cases):
    n = int(input())
    arrays = []
    if n != 0:
        for _ in range(n):
            arrays.append(list(input().split()))
        output_list.append(maximizing(arrays))
    else:
        output_list.append(-400)
for output in output_list:
    print(output)
print(sum(output_list))
