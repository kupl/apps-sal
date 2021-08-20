from collections import Counter


def tickets(people):
    bills = Counter({25: 0, 50: 0, 100: 0})
    required = {50: [Counter({25: 1})], 100: [Counter({25: 1, 50: 1}), Counter({25: 3})]}

    def check_required(person):
        for require in required[person]:
            if bills & require == require:
                bills.subtract(require)
                return True
        return False
    for person in people:
        bills[person] += 1
        if person > 25 and (not check_required(person)):
            return 'NO'
    return 'YES'
