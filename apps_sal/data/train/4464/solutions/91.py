def feast(beast, dish):
    start = beast.startswith(dish[:1])
    end = beast.endswith(dish[-1:])
    return start and end

