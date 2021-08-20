def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


n = int(input())
l = []
box = 0
for i in range(n):
    a = int(input())
    l.append(a)
l.sort(reverse=True)
for i in range(n):
    if l[i] != 0:
        for j in range(1, n):
            if l[j] != 0:
                if l[j] * 2 <= l[i]:
                    box = box + 1
                    l[i] = 0
                    l[j] = 0
                    break
l = remove_values_from_list(l, 0)
print(box + len(l))
