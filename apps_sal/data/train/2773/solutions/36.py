def calculate_years(principal, interest, tax, desired):
    #     raise NotImplementedError("TODO: calculate_years")
    years = 0
    if desired <= principal:
        return 0
    total_summ = principal
    while total_summ <= desired:

        summ_year = total_summ * interest
        summ_tax = summ_year * tax
        total_summ += summ_year - summ_tax
        print(total_summ)
        years += 1
        if total_summ >= desired:
            return years
