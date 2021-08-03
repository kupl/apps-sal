crystals = int(input())
li = list(map(int, input().split()))
a = li.sort()
points = 0
health = int(input())
pointer = -1
for i in range(len(li)):
    if health >= li[i]:
        health = health - li[i]
        points += 1
        li[i] = 0
    else:
        if points >= 1 and li[pointer] != 0:
            points -= 1
            health += li[pointer]
            pointer -= 1
            if health >= li[i]:
                health = health - li[i]
                points += 1
                li[i] = 0
        else:
            break
print(points)
