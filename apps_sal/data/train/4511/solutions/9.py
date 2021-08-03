def permute_a_palindrome(input):
    a = 'abcdefghijklmnopqrstuvwxyz'
    times = [0] * len(a)
    if input == "":
        return True
    if len(input) % 2 == 0:
        for x in range(0, len(a)):
            times[x] = input.count(a[x])
        print(times)
        for y in times:
            if not y % 2 == 0:
                return False
        else:
            return True
    else:
        count = 0
        for x in range(0, len(a)):
            times[x] = input.count(a[x])
        for y in times:
            if not y % 2 == 0 and count > 0:
                return False
            if not y % 2 == 0:
                count += 1
        else:
            return True
