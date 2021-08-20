from numbers import Real


class TaxCalculator(object):

    def __init__(self, bands, highest_rate):
        self.__table = list(self._get_table(bands, highest_rate))

    @staticmethod
    def _get_table(bands, highest_rate):
        (lower_bound, cumulative_tax) = (0.0, 0.0)
        for (upper_bound, rate) in bands:
            yield (lower_bound, rate, cumulative_tax)
            cumulative_tax += (upper_bound - lower_bound) * rate
            lower_bound = upper_bound
        yield (lower_bound, highest_rate, cumulative_tax)

    def __call__(self, amount):
        if isinstance(amount, Real):
            for (lower_bound, rate, cumulative_tax) in reversed(self.__table):
                if amount >= lower_bound:
                    return round((amount - lower_bound) * rate + cumulative_tax, 2)
        return 0.0


tax_calculator = TaxCalculator([(10.0, 0.1), (20.0, 0.07), (30.0, 0.05)], 0.03)
