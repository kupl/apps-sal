t = int(input())
while t:
    n = int(input())
    notes = [int(x) for x in input().split()]
    count = []
    for i in range(1, 9):
        count.append(notes.count(i))
    print(min(count))
    t -= 1
