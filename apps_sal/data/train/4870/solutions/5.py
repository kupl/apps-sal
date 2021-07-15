def redistribute_wealth(wealth):
    val = sum(wealth)/len(wealth)
    wealth[:] = map(lambda x : val,wealth)
