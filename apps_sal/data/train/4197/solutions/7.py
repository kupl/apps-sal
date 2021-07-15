def top3(products, amounts, prices):
    catalog = {n:amounts[i] * prices[i] for i,n in enumerate(products)}
    return sorted(catalog, key=catalog.get, reverse=True)[:3]
