def position():
    size = int(input())
    l = list(map(int, input().split()))
    pos = int(input())
    key = l[pos - 1]
    sortArray = sorted(l)
    for i in range(size):
        if(sortArray[i] == key):
            return i + 1


for _ in range(int(input())):
    print(position())
