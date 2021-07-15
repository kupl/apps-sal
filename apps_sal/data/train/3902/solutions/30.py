import unittest

PERCENT = 0.01


def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price * discount * PERCENT)
    
    
class TestDutyFree(unittest.TestCase):
    def test_duty_free(self):
        self.assertEqual(duty_free(price=12, discount=50, holiday_cost=1000), 166)

