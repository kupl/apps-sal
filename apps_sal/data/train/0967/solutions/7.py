# cook your dish here
def subset_sum(numbers, target, partial=[]):
    count = 0
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        count += 1
        return 1
    if s >= target:
        return 0  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        count += subset_sum(remaining, target, partial + [n])
    return count


t = int(input())
for i in range(t):
    input()
    n = int(input())
    s = list(map(int, input().split()))
    print(subset_sum(s, n))
