ENGLISH_NUMS = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 15: 'fifteen', 18: 'eighteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def name_that_number(x):
    return ENGLISH_NUMS.get(x, ENGLISH_NUMS[x % 10] + 'teen' if x < 20 else ENGLISH_NUMS[x - x % 10] + ' ' + ENGLISH_NUMS[x % 10])
