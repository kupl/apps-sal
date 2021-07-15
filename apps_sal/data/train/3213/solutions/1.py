def sum_of_a_beach(beach):
    return sum(beach.lower().count(fun) for fun in ["sand", "water", "fish", "sun"])
