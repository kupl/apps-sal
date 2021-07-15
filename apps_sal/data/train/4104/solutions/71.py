def max_tri_sum(numbers):
  num_set = list(set(numbers))
  sorted_nums = sorted(num_set, reverse=True)
  return sum(sorted_nums[0:3])
