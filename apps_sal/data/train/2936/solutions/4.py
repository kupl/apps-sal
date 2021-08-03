def num_of_open_lockers(n):
    return int(n ** 0.5)

# def num_of_open_lockers_not_opt(n):
#    nums = []
#    for i in xrange(0, n):
#        nums.append(False)
#
#    for i in xrange(1, n + 1):
#        for j in xrange(1, n + 1):
#            if j % i == 0:
#                nums[j - 1] = not nums[j - 1]
#
#    return nums.count(True)
