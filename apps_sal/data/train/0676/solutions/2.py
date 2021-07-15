t = int(input())
result = []
for i in range(t):
    n = int(input())
    names = input()
    names_list = names.split()
    unique_names = list(set(names_list))
    count = []
    for i in unique_names:
        counting = 0
        for j in names_list:
            if i == j:
                counting += 1
        count.append(counting)
    count_1 = 0
    for i in count:
        if i == max(count):
            count_1 += 1
    if count_1 == 1:
        result.append(unique_names[count.index(max(count))])
    else:
        a = []
        b = max(count)
        while max(count) == b:
            a.append(unique_names[count.index(max(count))])
            count[count.index(max(count))] = 0
        a.sort()
        result.append(a[0])
for i in result:
    print(i)

