r, c, n = map(int, input().split())
coordinates = []
coordinates_1, coordinates_2 = {}, {}
for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append([x, y])
for i in coordinates:
    if(i[0] in coordinates_1):
        coordinates_1[i[0]] += 1
    else:
        coordinates_1[i[0]] = 1
    if(i[1] in coordinates_2):
        coordinates_2[i[1]] += 1
    else:
        coordinates_2[i[1]] = 1
print(max(coordinates_1.values()) + max(coordinates_2.values()))
