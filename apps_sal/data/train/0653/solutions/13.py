crystel = int(input())
cry_val = list(map(int, input().split()))
laser = int(input())
(point, iterr) = (0, 0)
count = 1
point_mx = [0]
cry_val.sort()
while count <= crystel:
    if cry_val[iterr] <= laser:
        point += 1
        point_mx.append(point)
        laser -= cry_val[iterr]
        iterr += 1
        count += 1
    else:
        laser += cry_val[-1]
        cry_val.remove(cry_val[-1])
        point -= 1
        count += 1
print(max(point_mx))
