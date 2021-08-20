N = int(input())
one = two = 0
middles = []
for i in range(N):
    array = list(map(int, input().split()))[1:]
    size = len(array) - 1
    middle = size // 2
    for i in range(middle):
        one += array[i]
    for i in range(middle + 1, len(array)):
        two += array[i]
    if len(array) % 2 == 1:
        middles.append(array[middle])
    else:
        one += array[middle]
middles = sorted(middles)
ONE = True
for i in range(len(middles) - 1, -1, -1):
    if ONE:
        one += middles[i]
        ONE = False
    else:
        two += middles[i]
        ONE = True
print(one, two)
