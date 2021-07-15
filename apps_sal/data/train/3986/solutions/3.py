def discover_original_price(discounted_price, sale_percentage):
    #your code here
    return round( discounted_price / (1 - sale_percentage/100.) , 2 )

