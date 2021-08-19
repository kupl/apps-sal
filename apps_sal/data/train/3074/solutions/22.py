import unittest


def growing_plant(up_speed, down_speed, desired_height):
    result = 0
    day = 0
    while True:
        day += 1
        result += up_speed
        if result >= desired_height:
            break
        result -= down_speed
        if result >= desired_height:
            break
    return day


class TestGrowingPlant(unittest.TestCase):

    def test_should_return_1_when_desiredheight_is_equal_less_than_upspeed(self):
        self.assertEqual(growing_plant(up_speed=10, down_speed=9, desired_height=4), 1)

    def test_growing_plant_common_case(self):
        self.assertEqual(growing_plant(up_speed=100, down_speed=10, desired_height=910), 10)
