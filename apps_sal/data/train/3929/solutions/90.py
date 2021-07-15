import unittest


def reverse(st):
    return ' '.join(st.split()[::-1]).strip()
    
    
class TestReverse(unittest.TestCase):
    def test_reverse(self):
        st = 'Hello World'
        actual = reverse(st)
        self.assertEqual(actual, 'World Hello')

