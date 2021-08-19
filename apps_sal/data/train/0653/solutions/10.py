n = int(input())
health = sorted(map(int, input().split()))
laser = int(input())
(left, right) = (0, len(health) - 1)
ans = 0
while left <= right:
    if health[left] <= laser:
        laser -= health[left]
        ans += 1
        left += 1
    else:
        if ans == 0 or left + 1 == right:
            break
        laser += health[right]
        ans -= 1
        right -= 1
print(ans)
