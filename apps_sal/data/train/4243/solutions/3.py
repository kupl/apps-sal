def find_average(array):
    if not array:
        return 0

    class SafeFloat(object):
        def __init__(self, val):
            super(SafeFloat, self).__init__()
            self.val = val

        def __eq__(self, float_val):
            def isclose(a, b):
                return abs(a - b) < 0.00000001
            return isclose(self.val, float_val)

        def __str__(self):
            return str(self.val)

    from numpy import mean
    return SafeFloat(mean(array))
