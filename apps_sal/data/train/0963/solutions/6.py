def get_count(hills):
    max_ = hills.index(max(hills))
    if not max_ or max_ == len(hills) - 1:
        return 1
    return 1 + min(get_count(hills[:max_]), get_count(hills[max_ + 1:]))


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_count(arr))
