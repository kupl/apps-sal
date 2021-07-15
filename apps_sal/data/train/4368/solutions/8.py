def cost(mins):
    price =30
    while mins > 60:
        mins-=30
        if mins>35:
            price+=10
        else:
            return price
    else:
        return price
