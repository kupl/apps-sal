count = 0
inp = input().split(" ")
inp = [int(x) for x in inp]
while inp[0] != 0:
    t = input().split(" ")
    t = [int(x) for x in t]
    s = sum(t) - t[-1]
    if s >= inp[1] and t[-1] <= 10:
        count += 1
    inp[0] -= 1
print(count)
