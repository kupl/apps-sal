class Solution:

    def complexNumberMultiply(self, a, b):
        (re_a, im_a) = map(int, a.replace('i', '').split('+'))
        (re_b, im_b) = map(int, b.replace('i', '').split('+'))
        return str(re_a * re_b - im_a * im_b) + '+' + str(re_a * im_b + re_b * im_a) + 'i'
