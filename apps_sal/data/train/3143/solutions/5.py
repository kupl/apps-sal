num2words1 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
num2words2 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def sort_by_name(arr):
    return sorted(arr, key=lambda x: words(x))


def words(n):
    res = []
    if n >= 100:
        res.append(num2words1[n // 100])
        res.append("hundred")
        n -= n // 100 * 100
    if n >= 20:
        res.append(num2words2[n // 10])
        n -= n // 10 * 10
    if n > 0:
        res.append(num2words1[n])
    if not res:
        res.append("zero")
    return " ".join(res)
