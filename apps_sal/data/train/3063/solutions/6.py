def mix_fruit(arr):
    prices = {'banana': 5, 'orange': 5, 'apple': 5, 'lemon': 5, 'grapes': 5, 'avocado': 7, 'strawberry': 7, 'mango': 7}
    return round(sum(prices[f.lower()] if f.lower() in prices else 9 for f in arr) / len(arr))
