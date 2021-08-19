test_cases = int(input())


def canMakeTemple(strips, strips_height):
    check = 'yes'
    if strips % 2 != 0 and strips_height[strips // 2] == strips // 2 + 1:
        (left, right) = (0, strips - 1)
        for i in range(strips // 2):
            if strips_height[i] != strips_height[strips - i - 1]:
                check = 'no'
                break
    else:
        check = 'no'
    return check


for i in range(test_cases):
    strips = int(input())
    strips_height = list(map(int, input().split()))
    print(canMakeTemple(strips, strips_height))
