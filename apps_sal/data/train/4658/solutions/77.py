def max_product(lst, n_largest_elements):
  nums = sorted(lst)
  product = 1
  for num in nums[-(n_largest_elements):]:
    product = product * num
  return product
