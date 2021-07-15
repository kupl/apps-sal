_ = {True:'odd',False:'even'}
def odd_or_even(arr):
    return _.get(sum(arr)%2)
