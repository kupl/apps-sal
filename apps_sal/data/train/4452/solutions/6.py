def maximum_product_of_parts(n):
    products = []
    n = str(n)
    l = len(n)
    for i in range(1, l - 1):
        for j in range(i + 1, l):
            k = int(n[:i]) * int(n[i:j]) * int(n[j:l])
            products.append(k)
    return max(products)
