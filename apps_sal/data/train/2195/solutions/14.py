def count_sort(mass, st):
    i = st
    while i < len(mass):
        if mass[i] != mass[st]:
            break
        i += 1
    return i - st


n = int(input())

a = [int(x) for x in input().split(" ")]

a.sort()

i = a.count(a[0])
left = i
res = n - left
while i < len(a):
    count = count_sort(a, i)
    i += count
    left -= count
    if left < 0:
        res += left
        left = 0
    left += count

print(res)
