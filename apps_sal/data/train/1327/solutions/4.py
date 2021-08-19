t = int(input())
for i in range(t):
    (n, q) = input().split()
    cities = [int(x) for x in input().split()]
    cities_sort = cities.copy()
    cities_sort.sort()
    for j in range(int(q)):
        (q1, q2) = [int(x) for x in input().split()]
        a = cities[q1 - 1]
        b = cities[q2 - 1]
        if a > b:
            c = a
            a = b
            b = c
        pos_a = cities_sort[::1].index(a)
        pos_b = len(cities_sort) - 1 - cities_sort[::-1].index(b)
        print(q2 - q1 + b - a, pos_b - pos_a + 1)
