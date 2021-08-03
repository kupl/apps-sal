n, q = list(map(int, input().split()))
final = []
height = list(map(int, input().split()))
for k in range(0, q):
    b = input().split()
    if int(b[0]) == 1:
        step = int(b[1]) - 1
        for k in range(0, int(b[2])):
            temp = 0
            j = 1
            while j in range(1, 101) and temp == 0 and step + j < n:
                if height[step + j] > height[step]:
                    step = step + j
                    temp = 1
                j += 1
        final.append(step + 1)
    elif int(b[0]) == 2:
        for k in range(int(b[1]) - 1, int(b[2])):
            height[k] = height[k] + int(b[3])
for l in range(0, len(final)):
    print(final[l])
