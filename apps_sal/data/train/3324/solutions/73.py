def sale_hotdogs(customers):
    # price changes depending on customers val
    price = 100 if customers < 5 else 95 if 5 <= customers < 10 else 90

    return customers * price
