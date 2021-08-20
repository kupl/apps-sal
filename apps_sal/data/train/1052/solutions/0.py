from collections import deque
T = int(input())


def break_down(num):
    count = 0
    while len(num) != 1:
        temp = 0
        for i in range(0, len(num)):
            temp = temp + int(num[i])
        num = str(temp)
        count = count + 1
    return (int(num), count)


def digit_sum(num):
    temp = 0
    for i in range(0, len(num)):
        temp = temp + int(num[i])
    num = temp
    return num


while T:
    queue = deque()
    count_n = 0
    count_d = 0
    T = T - 1
    (N, d) = [i for i in input().split()]
    (n, count_n) = break_down(N)
    (D, count_D) = break_down(d)
    dic = {}
    if D == 1 or D == 2 or D == 4 or (D == 5) or (D == 7) or (D == 8):
        mini = 1
    elif D == 3 or D == 6:
        mini = min(digit_sum(str(n + 3)), digit_sum(str(n + 6)), digit_sum(str(n + 9)))
    else:
        mini = n
    queue.append((int(N), 0))
    ele = int(N)
    count = 0
    while len(queue) != 0:
        (ele, count) = queue.popleft()
        if ele == mini:
            break
        elif len(str(ele)) == 1:
            temp1 = ele + int(d)
            queue.append((temp1, count + 1))
        else:
            temp2 = digit_sum(str(ele))
            temp1 = ele + int(d)
            queue.append((temp2, count + 1))
            queue.append((temp1, count + 1))
    print(ele, count)
