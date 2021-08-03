import unittest


def vert_mirror(strng):
    return '\n'.join(word[::-1] for word in strng.split('\n'))


def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1])


def oper(fct, s):
    return fct(s)


class TestVertAndHorMirror(unittest.TestCase):
    def test_vert_mirror(self):
        fct, s = vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"
        actual = oper(fct, s)
        self.assertEqual(actual, "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")

    def test_hor_mirror(self):
        fct, s = hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"
        actual = oper(fct, s)
        self.assertEqual(actual, "yeCt\nCSbg\nJVhv\nlVHt")
