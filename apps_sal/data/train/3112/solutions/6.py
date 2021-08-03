def avoid_obstacles(arr):
    if min(arr) == 1 and max(arr) == 100:
        return 101
    landed = True
    for max_jump in range(2, 100):
        n = max_jump
        landed = True
        while n <= 100:
            for i in range(len(arr)):
                if n == arr[i]:
                    landed = False
                    break
            n += max_jump
        if landed:
            return max_jump
