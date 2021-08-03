
def calc(cards):

    queue = [(0, (0, len(cards) - 1))]
    counter = 1
    multiplier = 1
    global_max = 0
    while True:

        hold = {}

        for _ in range(counter):

            bonus, indices = queue.pop(0)
            if indices[0] > indices[1]:
                return global_max

            take_right = (indices[0], indices[1] - 1)
            bonus_right = bonus + cards[indices[1]] * (2**multiplier)
            take_left = (indices[0] + 1, indices[1])
            bonus_left = bonus + cards[indices[0]] * (2**multiplier)

            if take_left in hold:
                hold[take_left] = max(hold[take_left], bonus_left)

            else:
                hold[take_left] = bonus_left

            if take_right in hold:
                hold[take_right] = max(hold[take_right], bonus_right)

            else:
                hold[take_right] = bonus_right

            global_max = max(global_max, bonus_left, bonus_right)

        queue.extend([(hold[cards], cards) for cards in hold])

        counter += 1
        multiplier += 1

    return global_max
