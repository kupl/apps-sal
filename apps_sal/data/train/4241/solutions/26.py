# Boil it down to arythmetic progression
def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number: return 0
    n = int((end_number - begin_number)/step) # this n does not count begin_number as a first "step", so we'll have to do +1 in the formula below
    end_number = begin_number + step * n      # make sure the end belongs to the progression
    return int((begin_number + end_number) * (n + 1) * 0.5)
