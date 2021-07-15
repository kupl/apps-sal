def calculate_years(principal, interest, tax, desired):
    
    year_count = 0
    
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        
        year_count += 1
        
    return year_count

