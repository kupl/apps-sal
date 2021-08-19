import unittest


def seven(m):

    def _calc_last_rest(num):
        return (int(str(num)[-1]), int(str(num)[:-1]))
    if m == 0:
        return (0, 0)
    cnt = 0
    (last, rest) = _calc_last_rest(m)
    while True:
        cnt += 1
        result = rest - 2 * last
        if len(str(result)) <= 2:
            return (result, cnt)
        (last, rest) = _calc_last_rest(result)


class TestSeven(unittest.TestCase):

    def test_seven(self):
        m = 1603
        actual = seven(m)
        self.assertEqual(actual, (7, 2))

    def test_seven_second_case(self):
        m = 1021
        actual = seven(m)
        self.assertEqual(actual, (10, 2))

    def test_seven_when_m_is_0(self):
        m = 0
        actual = seven(m)
        self.assertEqual(actual, (0, 0))
