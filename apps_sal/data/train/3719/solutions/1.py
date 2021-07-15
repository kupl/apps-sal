# The linear relashionship is obvious taking a couple a informations (L1,H1) and (L2,H2)
# One gets 3.9354838709677433 = (H1-H2)/(L1-L2) and beta = H1-3.9354838709677433*H1

def starting_mark(height):
    return round(3.9354838709677433*height+3.4680645161290293,2)
