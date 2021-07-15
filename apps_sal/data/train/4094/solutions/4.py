def count_positives_sum_negatives(arr):
  output = []
  if arr:
    output.append(sum([1 for x in arr if x > 0]))
    output.append(sum([x for x in arr if x < 0]))
  return output
