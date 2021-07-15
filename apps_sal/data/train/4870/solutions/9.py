def redistribute_wealth(wealth):
    s=sum(wealth)/len(wealth)
    for i in range(len(wealth)):
        wealth[i]=s
