def michael_pays(costs):
    if costs < 5:
        michael = costs
    else:
        kate = min(costs / 3, 10)
        michael = costs - kate
    return round(michael, 2)
