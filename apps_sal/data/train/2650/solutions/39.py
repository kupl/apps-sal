N, L = map(int, input().split())

str_list = []

for w in range(N):
    str_list.append(input())

output = "".join(sorted(str_list))
print(output)
