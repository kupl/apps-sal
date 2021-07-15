def shortest_steps_to_num(num):
    return 0 if num == 1 else 1 + shortest_steps_to_num(num - 1 if num % 2 else num / 2)

