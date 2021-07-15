def find_discounted(prices):
    if prices == "":
        return ""
    out = []
    prices = [int(x) for x in prices.split(" ")]
    for price in prices:
        if int(price/0.75) in prices:
            prices.remove(int(price/0.75))
            out.append(str(price))
    return " ".join(out)
