def michael_pays(costs):
    kate = round((costs / 3), 2)
    if costs < 5:
        return round(costs, 2)
    return round(costs - kate, 2) if kate <= 10 else round(costs - 10, 2)
