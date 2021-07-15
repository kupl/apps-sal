def shortest_steps_to_num(n):
    return (
        0 if n == 1 else
        1 + shortest_steps_to_num(n-1) if n % 2 else
        1 + shortest_steps_to_num(n//2)
    )
