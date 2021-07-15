def min_sum(arr):
    # Your code here
    toplam=0
    while True:
        buyuk=max(arr)
        arr.remove(buyuk)
        kucuk=min(arr)
        arr.remove(kucuk)
        toplam+=buyuk*kucuk
        if len(arr)==0:
            return toplam
    pass
