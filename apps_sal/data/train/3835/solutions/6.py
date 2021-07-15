def find_discounted(prices):
    prices=list(map(int,prices.split()))
    discounted=[]
    while(prices):
        price=prices.pop()
        discount=int(price*0.75)
        prices.remove(discount)
        discounted.append(discount)
    return " ".join(map(str,discounted[::-1]))
