def find_combinations(list, sum):
    if not list:
        if sum == 0:
            return [[]]
        return []
    return find_combinations(list[1:], sum) + [[list[0]] + tail for tail in find_combinations(list[1:], sum - list[0])]


for tc in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    if len(find_combinations(a, k)) == 0:
        print('NO')
    else:
        print('YES')
