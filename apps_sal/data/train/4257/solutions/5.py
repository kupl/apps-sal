calculate_probability=lambda n,d=365,f=__import__('math').factorial:n>d or round(1-f(d)//f(d-n)/d**n,2)
