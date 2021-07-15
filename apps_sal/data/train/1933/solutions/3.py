class Solution:
     def complexNumberMultiply(self, a, b):
         """
         :type a: str
         :type b: str
         :rtype: str
         """
         
         # a( e + f ) * b( g + h )
         
         
         ae, af = a.split('+')
         af = af[:-1]
         ae, af = int(ae), int(af)
         
         bg, bh = b.split('+')
         bh = bh[:-1]
         bg, bh = int(bg), int(bh)
         
         
         ae_bg = ae * bg
         
         ae_bh = ae * bh
         af_bg = af * bg
         
         af_bh = af * bh
         
         first_term = ae_bg + (-1) * af_bh
         second_term = ae_bh + af_bg
         
         format_str = '{}+{}i'.format(str(first_term), str(second_term))
         
         return format_str
         
         
         

