def Guess_it(n, m):

    def get_sum_balls(a, b, c): return sum([a, b, c])
    def get_sum_mass(a, b, c): return sum([a * 5, b * 4, c * 3])

    green_max = min(m // 5, n)
    red_max = min(m // 4, n)

    result = []

    for green_ball in range(0, green_max + 1):
        for red_ball in range(0, red_max + 1):
            blue_ball = abs(n - (green_ball + red_ball))

            x = get_sum_balls(green_ball, red_ball, blue_ball)
            y = get_sum_mass(green_ball, red_ball, blue_ball)

            if x == n and y == m:
                result.append([green_ball, red_ball, blue_ball])

    return result
