n, m = [int(x) for x in input().split()]
coordinates = []
for i in range(n):
    coordinates.append([int(y) for y in input().split()])
hyp = (1+m*m)**(1/2)
cosx = 1/hyp
sinx = m/hyp
for point in coordinates:
    point[0], point[1] = (cosx*point[0] + sinx*point[1], -sinx*point[0] + cosx*point[1])

l = max(a[0] for a in coordinates) - min(a[0] for a in coordinates)
b = max(a[1] for a in coordinates) - min(a[1] for a in coordinates)

print(2*(l+b))
