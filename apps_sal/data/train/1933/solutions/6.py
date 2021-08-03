class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def parse_complex(s):
            real, image = s.split('+')
            return int(real), int(image[:-1])

        r_a, i_a = parse_complex(a)
        r_b, i_b = parse_complex(b)

        def construct_complex(real, image):
            return str(real) + '+' + str(image) + 'i'

        return construct_complex(r_a * r_b - i_a * i_b, r_a * i_b + r_b * i_a)
