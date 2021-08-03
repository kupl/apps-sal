def top3(products, amounts, prices):
    info = {}

    for index in range(len(products)):
        info[products[index]] = amounts[index] * prices[index]

    return sorted(info, key=lambda n: info[n], reverse=True)[:3]
