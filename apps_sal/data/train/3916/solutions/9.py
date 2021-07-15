def mean_vs_median(numbers):
  median = sorted(numbers)[len(numbers)//2]
  mean = float(sum(numbers)) / len(numbers)
  
  return 'mean' if mean > median else 'median' if median > mean else 'same'
