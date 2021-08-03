def top3(products, amounts, prices):
    result = {products[i]: amounts[i] * prices[i] for i in range(len(products))}
    result = list(sorted(result.items(), key=lambda x: x[1], reverse=True))
    return [i[0] for i in result[:3]]
