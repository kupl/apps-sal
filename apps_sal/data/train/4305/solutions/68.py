def digit_sum(string):
 return sum([int(x) for x in string])
 
def order_weight(string):
 weights = sorted(string.split())
 return " ".join(sorted(weights, key=digit_sum))
