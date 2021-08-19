n = int(input())
br = [int(i) for i in input().split()]
n = len(br)
alt_count = 0
prev_alt = -1
max_alt = 0

flag1 = flag2 = 0
start1 = start2 = max1 = max2 = 0
help_arr = [[0, 0]]

for i in range(n):
    if br[i] == 1:
        if flag1 == 0:
            start1 = i
        flag1 += 1
    elif br[i] == 2:
        flag1 -= 1
        if flag1 == 0 and i - start1 > max1:
            max1 = i - start1
            #print(start1, i)
    elif br[i] == 3:
        if flag2 == 0:
            start2 = i
        flag2 += 1
    elif br[i] == 4:
        flag2 -= 1
        if flag2 == 0 and i - start2 > max2:
            max2 = i - start2
    x = 0
    if br[i] == 1 or br[i] == 3:
        if help_arr[-1][1] != br[i]:
            x = 1
        help_arr.append([help_arr[-1][0] + x, br[i]])
        if help_arr[-1][0] > max_alt:
            max_alt = help_arr[-1][0]
    else:
        help_arr.pop(-1)
if 1 not in br:
    max1 = -1
if 3 not in br:
    max2 = -1
print(max_alt, max1 + 1, max2 + 1)
