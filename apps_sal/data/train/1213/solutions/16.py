def secretRecipe(x1, x2, x3, v1, v2):
    dist1 = abs(x3 - x1) / v1
    dist2 = abs(x3 - x2) / v2
    if dist1 < dist2:
        print('Chef')
    elif dist1 > dist2:
        print('Kefa')
    else:
        print('Draw')
    return


t = int(input())
for _ in range(t):
    (x1, x2, x3, v1, v2) = map(int, input().split())
    secretRecipe(x1, x2, x3, v1, v2)
