import math

def calLen(cam1, cam2, bird):
    a = math.sqrt((cam1[0]-bird[0])**2 + (cam1[1]-bird[1])**2)
    b = math.sqrt((cam2[0]-bird[0])**2 + (cam2[1]-bird[1])**2)
    c = math.sqrt((cam1[0]-cam2[0])**2 + (cam1[1]-cam2[1])**2)

    return a,b,c

def calculateAngle(a,b,c):
    return math.acos((a**2 + b**2 - c**2)/(2*a*b))

# def best_angle()

# def brute(n,cams,bird):
    # angles = []
    # for i in range(n):
    #     temp = [0]*n
    #     angles.append(temp)
    #     for j in range(i+1,n):
    #         a,b,c = calLen(cams[i],cams[j],bird)
    #         angles[i][j] = (calculateAngle(a,b,c))
    # print(angles)        
    # ans = 0
    # for i in range(n):
        
    #     while 

def angle2(cam1, cam2, bird):
    a, b, c = calLen(cam1, cam2, bird)
    return math.acos((a**2 + b**2 - c**2)/(2*a*b))

def backtrack(s, vertices, order):
    global res

    flag9 = 0
    for a in range(0, len(vertices)):
        if vertices[a] != 0:
            flag9 = 1
            break
    if flag9==0:
        # if s > res:

        # print(order)
        res = max(s, res)
        return
    for a in range(0, len(vertices)):
        for b in range(0, len(vertices)):
            if vertices[a] and vertices[b]:
                n1 = vertices[a]
                n2 = vertices[b]
                vertices[a] = 0
                vertices[b] = 0
                backtrack(s + angle2(n1, n2, bird), vertices,order + [vertices[a],vertices[b]] )
                vertices[a] = n1
                vertices[b] = n2

from random import randint

for h in range(int(input())):
    n = int(input())
    cams = list(map(lambda x: (int(x), 0), input().strip().split())) 
    # cams = [(randint(1,33),0) for a in range(0, n)]
    cams1 = [i for i in cams]
    # print(cams,cams1)
    bird = list(map(int, input().strip().split()))
    # bird = [randint(0,33),randint(1,33)]

    # brute(n,cams,bird)

    ans = 0
    i = 0
    i2 = [0,0]
    i4 = [0,0]

    while set(cams1) != {0}:

        # print(set(cams1) )
        i = 0
        # i2 = [0,0]
        for a in range(0, len(cams1)):
            for b in range(a+1, len(cams1)):
                if cams1[a] and cams1[b]:
                    if abs( cams1[a][0] - cams1[b][0]) >= i:
                        i = abs( cams1[a][0] - cams1[b][0])
                        i2 = [cams1[a], cams1[b ]]
                        i4=[a, b]
                        # print(i2)
        ans += angle2(i2[0],i2[1], bird)
        cams1[i4[0]] = 0
        cams1[i4[1 ]] = 0
    print(ans)

    res = 0
    # backtrack(0,cams,[])
    # print(res)



