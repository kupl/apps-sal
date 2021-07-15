def mix_fruit(arr):
    d = {'banana':5,'orange':5,'apple':5,'lemon':5,'grapes':5,'avocado':7,'strawberry':7,'mango':7}
    return round(sum(d.get(i.lower(),9) for i in arr)/len(arr))
