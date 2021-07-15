def over_the_road(address, n):
    totale=2*n
    x=(totale-address)//2
    y=(address-1)//2
    if address % 2 ==0:
        z= -totale+1 + x*4
        return (address + z)
    else:
        z= totale-1 - y*4
        return(address + z)
        
        

