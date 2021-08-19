import unittest


def correct_tail(body, tail):
    last_char_of_body = body[-1]
    return True if last_char_of_body == tail else False


class TestCorrectTail(unittest.TestCase):

    def test_should_return_false_when_last_of_char_of_body_is_not_equal_tail(self):
        self.assertFalse(correct_tail(body='Emu', tail='m'))

    def test_should_return_true_when_last_of_char_of_body_is_equal_tail(self):
        self.assertTrue(correct_tail(body='Fox', tail='x'))
