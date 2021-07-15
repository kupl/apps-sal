def match(usefulness, months):
    decay, needs = 0.15, 100
    return "Match!" if needs * (1 - decay)**months <= sum(usefulness) else "No match!"
