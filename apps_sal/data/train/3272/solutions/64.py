import statistics


def find_average(nums):
    try:
        return statistics.mean(nums)
    except:
        return 0
