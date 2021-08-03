from heapq import heappush, heappop
try:
    # Getting n, m, then initialising the lists
    n, m = list(map(int, input().split()))
    normal = []
    exe = []
    # As the problem states, we should do this n+m times.
    for i in range(0, (n + m)):
        get = int(input())
        # If the king has come, return the smallest(but biggest) element
        # For executing.
        if get == -1:
            c = -heappop(normal)
            exe.append(c)
        # Otherwise, push the negative value to normal
        else:
            heappush(normal, -get)
    # For loop to iterate through the executed people, and print them
    z = len(exe)
    for j in range(0, z):
        print(exe[j])
except:
    pass
