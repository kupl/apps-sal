from bisect import bisect


def happy_numbers(n):
    happy_list = []
    happy = {1}
    unhappy = set()
    for k in range(1, n + 1):
        i = k
        seen = set()
        while True:
            if i in happy:
                happy_list.append(k)
                happy |= seen
                break
            elif i in unhappy or i in seen:
                unhappy |= seen
                break
            seen.add(i)
            i = sum((int(d) ** 2 for d in str(i)))
    return happy_list


happy_list = happy_numbers(300000)


def performant_numbers(n):
    i = bisect(happy_list, n)
    return happy_list[:i]
