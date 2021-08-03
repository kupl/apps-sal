temp = [1, 2, 4, 8]
data = [0] * 1000000
data[2] = 1
data[3] = 1
data[5] = 1
data[9] = 1
data[4] = 1
data[6] = 1
data[10] = 1
data[8] = 1
data[12] = 1
data[16] = 1
while(len(temp) <= 100):
    for i in range(temp[len(temp) - 1], 2 * temp[len(temp) - 1] + 1):
        c = 0
        for j in range(0, len(temp)):
            if (data[i + temp[j]] == 0):
                c += 1
        if (c == len(temp)):
            temp.append(i)
            for j in range(0, len(temp)):
                data[i + temp[j]] = 1
            break
for i in range(int(input())):
    n = int(input())
    print(*temp[0:n], sep=" ")
    print(sum(temp[0:n]))
