def solve_small(numbers, n, f):
    found = False
    min_shield = 0
    min_pos = 0
    for pos in range(n):
        next_pos0 = pos % (n - 1)
        if numbers[next_pos0] > f:
            continue
        new_numbers = [_ for _ in numbers]
        new_numbers.insert(pos, 0)
        curr_pos = 0
        while len(new_numbers) > 2:
            next_pos = (curr_pos + 1) % len(new_numbers)
            if new_numbers[next_pos] <= 0:
                new_numbers[next_pos] -= new_numbers[curr_pos]
            elif new_numbers[curr_pos] > 0:
                new_numbers.pop(next_pos)
            else:
                pass
            if curr_pos >= len(new_numbers) - 1:
                curr_pos = 0
            else:
                curr_pos += 1
        (shield, min_f) = (-min(new_numbers), max(new_numbers))
        if min_f > f:
            continue
        shield += f
        found = True
        if not min_shield or min_shield > shield:
            min_shield = shield
            min_pos = pos
    if found:
        print('possible')
        return (min_pos + 1, min_shield)
    else:
        print('impossible')
        return (0, 0)


def solve_med(numbers, n, f):
    min_shield = 0
    min_pos = 0
    left_numbers = []
    right_numbers = [0] + [_ for _ in numbers]
    for pos in range(0, n):
        right_numbers.pop(0)
        if pos % 2:
            left_numbers.append(numbers[pos - 1])
        next_pos0 = pos % (n - 1)
        if numbers[next_pos0] > f:
            continue
        shield = f
        if pos % 2:
            shield += numbers[pos - 1]
        new_numbers = right_numbers + left_numbers
        jos_pos = len(new_numbers)
        new_pos = jos_pos
        factor = 2
        while new_pos > 1:
            if new_pos % 2:
                number = new_numbers[get_prev_multiple(jos_pos, factor)]
                number2 = numbers[get_prev_multiple_2(n - 1, pos, factor)]
                shield += number
            new_pos = new_pos // 2 + new_pos % 2
            factor *= 2
        if not min_shield or shield < min_shield:
            min_shield = shield
            min_pos = pos + 1
    if min_shield:
        print('possible')
    else:
        print('impossible')
    return (min_pos, min_shield)


def get_prev_multiple_2(n, pos, f):
    left_numbers = (pos - 1) // 2
    right_numbers = n - pos
    total_numbers = left_numbers + right_numbers
    number = total_numbers - total_numbers % f
    if number >= right_numbers:
        number = number - right_numbers
        return 2 * number
    else:
        return pos + number


def get_prev_multiple(n, f):
    return n - 1 - (n - 1) % f


def get_input_line():
    return input()


def solve_big(numbers, n, f):
    min_shield = 0
    min_pos = 0
    for pos in range(0, n):
        next_pos0 = pos % (n - 1)
        if numbers[next_pos0] > f:
            continue
        shield = f
        if pos % 2:
            shield += numbers[pos - 1]
        jos_pos = (pos - 1) // 2 + n - pos
        new_pos = jos_pos
        factor = 2
        over = False
        while new_pos > 1:
            if new_pos % 2:
                number = numbers[get_prev_multiple_2(n - 1, pos, factor)]
                shield += number
                if min_shield and shield >= min_shield:
                    over = True
                    break
            new_pos = new_pos // 2 + new_pos % 2
            factor *= 2
        if over:
            continue
        if not min_shield or shield < min_shield:
            min_shield = shield
            min_pos = pos + 1
    if min_shield:
        print('possible')
    else:
        print('impossible')
    return (min_pos, min_shield)


t = int(input())
for i in range(t):
    n = int(input())
    numbers = list(map(int, input().split(' ')))
    f = int(input())
    (min_pos, min_shield) = solve_small(numbers, n, f)
    if min_shield:
        print(min_pos, min_shield)
