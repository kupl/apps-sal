(n, l) = map(int, input().split())
string_list = [input() for i in range(n)]
string_list.sort()
ans = string_list[0]
for i in range(1, n):
    ans += string_list[i]
print(ans)
