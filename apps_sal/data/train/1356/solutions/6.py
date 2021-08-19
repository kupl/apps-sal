ans = [1]


def bell_numbers(start, stop):
    # Swap start and stop if start > stop
    if stop < start:
        start, stop = stop, start
    if start < 1:
        start = 1
    if stop < 1:
        stop = 1

    t = [[1]]  # Initialize the triangle as a two        -dimensional array
    c = 1  # Bell numbers count
    while c <= stop:
        if c >= start:
            yield t[-1][0]  # Yield the Bell number of the previous                 row
        row = [t[-1][-1]]  # Initialize a new row
        for b in t[-1]:
            row.append((row[-1] % 1000000007 + b % 1000000007) % 1000000007)  #                 Populate the new row
        c += 1  # We have found another Bell number
        t.append(row)  # Append the row to the triangle
        ans.append(row[-1])
    t = list(t)


b = []
b = bell_numbers(1, 1001)
x = eval(input())
count = 1
for i in b:
    count += 1
while(x > 0):
    y = eval(input())
    print(ans[y - 1] % 1000000007)
    x = x - 1
