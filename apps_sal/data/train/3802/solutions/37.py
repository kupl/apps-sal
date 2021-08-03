import unittest

TEN_MORE_HOOPS_MESSAGE = "Great, now move on to tricks"
NOT_TEN_MORE_HOOPS_MESSAGE = "Keep at it until you get it"


def hoop_count(n):
    return TEN_MORE_HOOPS_MESSAGE if n >= 10 else NOT_TEN_MORE_HOOPS_MESSAGE


class TestHoopCount(unittest.TestCase):
    def test_should_return_encouraging_message_when_getting_ten_more_hoops(self):
        n = 11
        actual = hoop_count(n)
        self.assertEqual(actual, TEN_MORE_HOOPS_MESSAGE)

    def test_should_return_encouraging_message_when_does_not_getting_ten_more_hoops(self):
        n = 3
        actual = hoop_count(n)
        self.assertEqual(actual, NOT_TEN_MORE_HOOPS_MESSAGE)
