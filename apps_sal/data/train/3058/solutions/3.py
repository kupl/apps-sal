def is_magical(s):
    return sum(s[::3]) == sum(s[1::3]) == sum(s[2::3]) == 15
