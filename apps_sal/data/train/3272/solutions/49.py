import statistics
def find_average(nums):
    if len(nums)==0:
        return 0
    else:
        return statistics.mean(nums)
