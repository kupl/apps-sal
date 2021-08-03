class Solution:
    def closestDivisors(self, num: int) -> List[int]:

        #         If I have 8, I will check for 9 also. For checking 9, I will check till half value of the number. so that i can #confirm that, its not a prime number, if it gor divided by any number.
        # In case of 10, first, I divide with 2, so the quotient will be 5. My limit will be set between 2 and 5. If there is #another couple of factors exist in between. I will take them. I will follow these steps, till divisor is less than #quotient. If I didnt get a suiatble pair, I will jump to num+2 and follow the same steps.

        #         N = num+1
        #         dvsr = 2
        #         quo = N
        #         flag = 0
        #         while(dvsr < quo and dvsr < N // 2):
        #             if N % dvsr == 0:
        #                 quo = int(N / dvsr)
        #                 flag = 1
        #             else:
        #                 dvsr += 1

        #         if flag == 1:
        #             return [dvsr, quo]

        #         N = num+2
        #         dvsr = 2
        #         quo = N
        #         while(dvsr < quo and dvsr < N // 2):
        #             if N % dvsr == 0:
        #                 quo = int(N / dvsr)
        #             else:
        #                 dvsr += 1

        #         return [dvsr, quo]

        # This approch is tedious, so, lets get the sqrt of the num+1 and num+2. If tehre exists a perfect square root, return that. Else, keep on decreasing the valaue unless you find one

        N1 = num + 1
        N2 = num + 2
        sqrt1 = int(N1**0.5) + 1
        sqrt2 = int((N2)**0.5) + 1

        while sqrt1 >= 2 or sqrt2 >= 2:
            if (N2) % sqrt2 == 0:
                return [sqrt2, int(N2 / sqrt2)]
            if N1 % sqrt1 == 0:
                return [sqrt1, int(N1 / sqrt1)]
            else:
                sqrt1 -= 1
                sqrt2 -= 1

        return [1, sqrt1]
