T = int(input())
outputs = []
while T > 0:
    inStr = input()
    inStr = list(map(int, inStr.split(' ')))
    finish = inStr[0]
    distancetoBolt = inStr[1]
    tigerAcceleration = inStr[2]
    boltSpeed = inStr[3]
    boltTime = finish / boltSpeed
    tigerTime = (2 * (distancetoBolt + finish) / tigerAcceleration) ** (1 / 2)
    if tigerTime <= boltTime:
        outputs.append('Tiger')
    else:
        outputs.append('Bolt')
    T -= 1
print(*outputs, sep='\n')
