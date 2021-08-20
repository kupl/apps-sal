(n, d) = [int(i) for i in input().split()]
xAxis = [int(i) for i in input().split()]
cnt = 0
temp = []
temp.append(xAxis[0])
for i in range(len(temp), len(xAxis)):
    temp.append(xAxis[i])
    if temp[-1] - temp[0] > d:
        cnt += (len(temp) - 2) * (len(temp) - 3) / 2
        del temp[0]
        while len(temp) > 1:
            if temp[-1] - temp[0] > d:
                cnt += (len(temp) - 2) * (len(temp) - 3) / 2
                del temp[0]
            else:
                break
    if i == len(xAxis) - 1 and temp[-1] - temp[0] <= d:
        cnt += len(temp) * (len(temp) - 1) * (len(temp) - 2) / (3 * 2)
print(int(cnt))
