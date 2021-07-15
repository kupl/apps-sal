import sys

n_discounts = int(sys.stdin.readline())
discount_values = [int(x) for x in sys.stdin.readline().split()]
n_items = int(sys.stdin.readline())
item_values = [int(x) for x in sys.stdin.readline().split()]

min_discount_req = 10000000
for discount_value in discount_values:
    min_discount_req = min(min_discount_req, discount_value)
item_values.sort(reverse=True)

index = 0
overall_price = 0
while index < n_items:
    n_left = min(min_discount_req, n_items - index)
    for i in range(n_left):
        overall_price += item_values[index+i]
    index += n_left + 2

print(overall_price)
    

