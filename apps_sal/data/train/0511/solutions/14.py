N = int(input())
a_list = list(map(int, input().split()))
all_xor = 0
res = []

for a in a_list:
    all_xor ^= a

for a in a_list:
    res.append(a ^ all_xor)

print((*res))

