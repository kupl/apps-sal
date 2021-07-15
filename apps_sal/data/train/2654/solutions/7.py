def michael_pays(costs):
    return round(costs, 2) if costs < 5 else round(max(costs-10, costs/3*2), 2)
