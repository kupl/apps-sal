num_points = int(input())
coords = [int(x) for x in input().split()]
coords.sort()
width = coords[num_points - 1] - coords[0]
height = coords[-1] - coords[num_points]
area1 = width * height
width2 = min((coords[i + num_points - 1] - coords[i] for i in range(num_points + 1)))
height2 = coords[-1] - coords[0]
area2 = width2 * height2
area = min(area1, area2)
print(area)
