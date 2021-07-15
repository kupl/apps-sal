def calculate_tip(amount, rating):
    
    error = 'Rating not recognised'
    ratings = {
        'terrible' : 0,
        'poor'     : 0.05,
        'good'     : 0.1,
        'great'    : 0.15,
        'excellent': 0.2, 
    }

    try:
        if isinstance(amount, str):
            return error

        v = ratings[rating.lower()]*amount

        if not v % 2 == 0: 
            return int(v+(1-(v%1)))
        else:
            return int(v)
        
    except KeyError:
        return error
