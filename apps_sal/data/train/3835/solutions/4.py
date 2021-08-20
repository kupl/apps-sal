def find_discounted(prices):
    discount = 0.25
    in_list = [int(p) for p in prices.split()]
    out_list = []
    while in_list:
        full_price = in_list.pop()
        discounted_price = int(full_price * (1 - discount))
        in_list.remove(discounted_price)
        out_list.append(discounted_price)
    out_list.reverse()
    ans = ' '.join((str(p) for p in out_list))
    return ans
