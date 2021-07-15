import unittest


def fold_to(distance):
    folding_count = 0
    meter_of_paper = 0.0001

    while meter_of_paper <= distance:
        folding_count += 1
        meter_of_paper = meter_of_paper * 2

    return folding_count if distance >= 0 else None
    
    
class TestFoldTo(unittest.TestCase):
    def test_fold_to_should_return_none_whne_given_distance_is_negative_one(self):
        distance = -1
        actual = fold_to(distance)
        self.assertEqual(actual, None)

    def test_fold_to(self):
        distance = 384000000
        actual = fold_to(distance)
        self.assertEqual(actual, 42)

