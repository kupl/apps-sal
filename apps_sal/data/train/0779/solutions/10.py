
"""

The first thing that comes to my mind is

while(len(arr)! = 2)
{
    sort(arr)
    last_two_average = (arr[-1]+arr[-2])/2
    arr = arr[:-3].append(last_two_average)
}
print((arr[0] + arr[1])/2)

This solution will mostly timed out because of the sorting in reach step

"""

testcase = int(input())
for z in range(testcase):
    N = int(input())
    arr = [int(d) for d in input().split()]
    while(N > 2):
        arr = sorted(arr)
        last_two_average = (arr[-1] + arr[-2]) / 2
        arr = arr[:-2]
        arr.append(last_two_average)
        N = N - 1
    print("{0:.8f}".format((arr[0] + arr[1]) / 2))
