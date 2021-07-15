def max_tri_sum(numbers):
    uniq = set(numbers)
    return sum([max(uniq), max(uniq - {max(uniq)}), max(uniq - {max(uniq)} - {max(uniq - {max(uniq)})})])
