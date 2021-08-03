def avoid_obstacles(arr):
    jump = 2

    while True:
        start_again = False

        for num in arr:
            if num % jump == 0:
                jump = jump + 1
                start_again = True
                break

        if not start_again:
            return jump
