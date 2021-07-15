def multi_table(number):
    return "\n".join(f"{n} * {number} = {n*number}" for n in range(1,11))
