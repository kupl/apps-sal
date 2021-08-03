n = int(input())
l = [int(i) for i in input().split(" ")]
l_up = l[:]
l_down = l[::-1]

for i in range(n - 1):
    if l_up[i + 1] <= l_up[i]:
        l_up[i + 1] = l_up[i] + 1
for i in range(n - 1):
    if l_down[i + 1] <= l_down[i]:
        l_down[i + 1] = l_down[i] + 1
l_down = l_down[::-1]

index = 0
add = False
for index in range(n - 1):
    if l_up[index] < l_down[index] and l_up[index + 1] >= l_down[index + 1]:
        if l_up[index + 1] == l_down[index + 1]:
            break
        else:
            add = True
            break
    if index == n - 2:
        index = 0
if add == False:
    l_final = l_up[:index + 1] + l_down[index + 1:]
    result = sum(l_final) - sum(l)
else:
    l_final = l_up[:index + 1] + l_down[index + 1:]
    result = sum(l_final) - sum(l) + 1


# print(index)
# print(l_up)
# print(l_down)
# print(l_final)
print(result)
