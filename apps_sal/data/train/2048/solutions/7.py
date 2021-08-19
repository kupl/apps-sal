from sys import stdin

n, k = [int(x) for x in stdin.readline().split()]
oK = k

c = sorted([int(x) for x in stdin.readline().split()])

l = 0
r = n - 1

low = c[0]
high = c[-1]

lowBuffer = 0
highBuffer = 0

while low < high:
    if low == c[l]:
        l += 1
    if high == c[r]:
        r -= 1

    if l * (c[l] - low) - lowBuffer > (n - r - 1) * (high - c[r]) - highBuffer <= k:
        #print(low,high,l,r,'highDown', (n-r-1)*(high-c[r])-highBuffer)

        k -= (n - r - 1) * (high - c[r]) - highBuffer
        lowBuffer += (n - r - 1) * (high - c[r]) - highBuffer
        highBuffer = 0
        high = c[r]

    elif (n - r - 1) * (high - c[r]) - highBuffer >= l * (c[l] - low) - lowBuffer <= k:
        # print(low,high,l,r,'lowUp',l*(c[l]-low)-lowBuffer)
        k -= l * (c[l] - low) - lowBuffer
        highBuffer += l * (c[l] - low) - lowBuffer
        lowBuffer = 0
        low = c[l]
    else:
        low += (lowBuffer + k) // l
        high -= (highBuffer + k) // (n - r - 1)
        k = 0
        break

if sum(c) % n == 0:
    print(max(0, high - low))
else:
    print(max(1, high - low))
