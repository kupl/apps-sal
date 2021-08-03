def top3(products, amounts, prices):
    comparison = {}
    topList = []
    for i in range(len(products)):
        comparison[products[i]] = amounts[i] * prices[i]
    [topList.append(k) for k, v in sorted(comparison.items(), key=lambda x: x[1], reverse=True)]
    return topList[:3]
