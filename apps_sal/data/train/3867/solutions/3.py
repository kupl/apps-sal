import re
rotten_pattern = re.compile("rotten")

def remove_rotten(bag_of_fruits):
  return [re.sub(rotten_pattern, "", fruit.lower()) for fruit in bag_of_fruits] if bag_of_fruits else []
