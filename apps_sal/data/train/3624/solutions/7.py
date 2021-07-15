def distribution_of_candy(candies):
    candies_upd = candies
    cnt = 0
    if len(candies) == 1:
        return [0, candies[0]]
    while candies.count(candies[0]) < len(candies) or candies_upd.count(candies_upd[0]) < len(candies_upd):
        if cnt > 0:
            candies = candies_upd
        candies_upd = []
        for i in range(len(candies)):           
            new = candies[i]
            if candies[i]%2 != 0:
                new +=1
            new-=(new/2)
            if i == 0:
                new+=(round(candies[-1]/2 +0.1))
            else:
                new +=(round(candies[i-1]/2 +0.1))
            candies_upd.append(new)
        
        cnt +=1
        
    return [cnt-1, candies[0]]

