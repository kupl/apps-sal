def hop_across(lst):
    def one_side(lst):
        i = 0
        steps = 0
        while i < len(lst):
            i += lst[i]
            steps += 1
        return steps
    return one_side(lst) + one_side(lst[::-1])
