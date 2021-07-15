def michael_pays(costs):
    return round(costs - min(0 if costs < 5 else 10, costs / 3), 2)
