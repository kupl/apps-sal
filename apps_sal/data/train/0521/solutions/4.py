import math

def calLen(cam1, cam2, bird):
    a = math.sqrt((cam1[0]-bird[0])**2 + (cam1[1]-bird[1])**2)
    b = math.sqrt((cam2[0]-bird[0])**2 + (cam2[1]-bird[1])**2)
    c = math.sqrt((cam1[0]-cam2[0])**2 + (cam1[1]-cam2[1])**2)

    return a,b,c

for h in range(int(input())):
    n = int(input())
    cams = list(map(lambda x: [int(x), 0], input().strip().split()))
    bird = list(map(int, input().strip().split()))
    cams.sort(key = lambda x:x[0])

    ans = 0
    for i in range(n//2):
        cam1 = cams[i]
        cam2 = cams[n-1-i]

        a, b, c = calLen(cam1, cam2, bird)
        ans += math.acos((a**2 + b**2 - c**2)/(2*a*b))
    print(ans)
