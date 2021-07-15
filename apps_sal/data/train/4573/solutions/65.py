def over_the_road(address, n):
        current = (n - address//2)*2
        if not address%2:
            current +=1
        return current
        

