def bmi(weight, height):
  bmi_val = weight / height**2
  return get_weight_class(bmi_val)

# bmi_ranges start open bound & end closed bound
def get_weight_class(bmi_val):
  bmi_ranges = [(0, 18.5), (18.5, 25), (25, 30), (30, float("inf"))]
  weight_classes = {
    (0, 18.5): "Underweight",
    (18.5, 25): "Normal",
    (25, 30): "Overweight",
    (30, float("inf")): "Obese",
  }
  # see what range bmi belongs to with binary search
  start = 0
  end = len(bmi_ranges) - 1

  while not(start > end):
    mid_i = start + abs(end - start)//2
    range_start, range_end = bmi_ranges[mid_i]

    if range_start < bmi_val <= range_end:
      return weight_classes[(range_start, range_end)]
    elif bmi_val <= range_start:
      end = mid_i - 1
    elif bmi_val > range_end:
      start = mid_i + 1

  raise ValueError("BMI value out of range.")

