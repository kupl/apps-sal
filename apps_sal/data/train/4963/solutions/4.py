def closest_multiple_10(x):
    return x - (x% 10) if x%10 < 5 else x - (x%10) + 10
