def solution(stones):
    counter = -1
    previous_stone = stones[0]

    for stone in stones:
        if previous_stone == stone:
            counter += 1

        else:
            previous_stone = stone

    return counter
