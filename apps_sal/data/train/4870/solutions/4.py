def redistribute_wealth(wealth):
    wealth[:] = len(wealth)*[sum(wealth)/float(len(wealth))]
