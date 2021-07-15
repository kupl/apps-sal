def process_data(data):
    product = 1
    
    for tuple in data:
        product *= tuple[0] - tuple[1]
        
    return product
  

