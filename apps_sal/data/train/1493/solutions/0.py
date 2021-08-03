def outOfIndex(boys, girls, COST):
    if COST == 0:
        return len(boys)
    else:
        total_cost = [abs(x - y) for x, y in zip(boys, girls)]
        total_cost = sum(total_cost)
        return total_cost


for _ in range(int(input())):
    COST = int(input())
    queue = input()
    B = queue.count('B')
    G = queue.count('G')
    boys = []
    girls = []
    if (abs(B - G) > 1):
        print(-1)
    else:
        if B > G:
            for c in range(len(queue)):
                if c % 2 != 0 and queue[c] == 'B':
                    boys.append(c)
                if c % 2 == 0 and queue[c] == 'G':
                    girls.append(c)
            print(outOfIndex(boys, girls, COST))
            boys.clear()
            girls.clear()
        elif B < G:
            for c in range(len(queue)):
                if c % 2 != 0 and queue[c] == 'G':
                    girls.append(c)
                if c % 2 == 0 and queue[c] == 'B':
                    boys.append(c)
            print(outOfIndex(boys, girls, COST))
            boys.clear()
            girls.clear()
        else:
            for c in range(len(queue)):
                if c % 2 != 0 and queue[c] == 'B':
                    boys.append(c)
                if c % 2 == 0 and queue[c] == 'G':
                    girls.append(c)
            attempt1 = outOfIndex(boys, girls, COST)
            boys.clear()
            girls.clear()
            for c in range(len(queue)):
                if c % 2 != 0 and queue[c] == 'G':
                    girls.append(c)
                if c % 2 == 0 and queue[c] == 'B':
                    boys.append(c)
            attempt2 = outOfIndex(boys, girls, COST)
            print(min(attempt1, attempt2))
            boys.clear()
            girls.clear()
