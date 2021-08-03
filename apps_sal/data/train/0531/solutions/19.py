
n = int(input())
sticks = []
count = 2

for i in range(n):
    inn = input().split(' ')
    sticks.append([int(inn[0]), int(inn[1])])
if len(sticks) < 2:
    print(len(sticks))
    return
area = [[sticks[0][0] - sticks[0][1], sticks[0][0]],

        [sticks[-1][0], sticks[-1][0] + sticks[-1][1]]

        ]

# print(sticks)
# print(area)
for i in sticks:
    area.append([i[0], i[0]])


def check(aa, hh):
    a = aa - hh
    h = aa
    flag = 0
    for i in area:
        if i == [aa, aa]:
            continue
        if i[0] == i[1] and a <= i[0] and h >= i[0]:
            flag = -1
            break
        if a <= i[0] and h >= i[0]:

            flag = -1
            break
        if a <= i[0] and h >= i[1]:

            flag = -1
            break
        if a <= i[1] and h >= i[1]:

            flag = -1
            break
        if a >= i[0] and h <= i[1]:

            flag = -1
            break
    if flag == 0:
        return [a, h]
    flag = 1
    a = aa
    h = aa + hh
    for i in area:
        if i == [aa, aa]:
            continue
        if i[0] == i[1] and a <= i[0] and h >= i[0]:
            flag = -1
            break
        if a <= i[0] and h >= i[0]:

            flag = -1
            break
        if a <= i[0] and h >= i[1]:

            flag = -1
            break
        if a <= i[1] and h >= i[1]:

            flag = -1
            break
        if a >= i[0] and h <= i[1]:

            flag = -1
            break
    if flag == 1:
        return [a, h]
    return -1


for i in sticks[1:-1]:
    temp = check(i[0], i[1])

    if temp == -1:
        continue
    count += 1
    area.append(temp)

print(count)
