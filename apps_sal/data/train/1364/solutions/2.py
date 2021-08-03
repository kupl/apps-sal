# cook your dish here
t = int(input())
for _ in range(t):
    n, c = list(map(lambda x: int(x), input().split()))
    hashmap = {}
    for i in range(0, n):
        x, y = list(map(lambda x: int(x), input().split()))
        mod_x = x % c
        mod_y = y % c
        if (mod_x, mod_y, x - y) not in hashmap:
            hashmap[(mod_x, mod_y, x - y)] = []
        hashmap[(mod_x, mod_y, x - y)].append((x, y))
    print(len(hashmap), end=" ")
    total_operations = 0

    for key in hashmap:
        hashmap[key] = sorted(hashmap[key], key=lambda x: x[0])
        initial = hashmap[key][len(hashmap[key]) // 2][0]

        for x, y in hashmap[key]:
            total_operations += abs((x - initial) // c)
    print(total_operations)
