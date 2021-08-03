class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        divisor_dict = {}

        def get_divisors(num):
            all_divisors = []
            divisor_set = set()
            for divisor_one in range(int(num**0.5), 0, -1):
                divisor_two = int(num / divisor_one)
                if divisor_one in divisor_set or divisor_two in divisor_set:
                    continue
                if num % divisor_one == 0:
                    divisor_set.add(divisor_one)
                    divisor_set.add(divisor_two)
                    all_divisors.append((divisor_one, divisor_two))
            return all_divisors

        closest_divisor = num * 2

        all_divisors = []
        for divisor in get_divisors(num + 1):
            all_divisors.append(divisor)
        for divisor in get_divisors(num + 2):
            all_divisors.append(divisor)

        print(all_divisors)
        return_divisor_pair = None
        for divisor in all_divisors:
            difference = divisor[0] - divisor[1]
            if difference < 0:
                difference *= -1
            if difference < closest_divisor:
                closest_divisor = difference
                return_divisor_pair = divisor

        return list(return_divisor_pair)
