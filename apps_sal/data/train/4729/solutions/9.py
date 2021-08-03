def numbers_of_letters(n):
    change = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
              "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    num, sol = "".join(change[x] for x in str(n)), []
    sol.append(num)
    while num != "four":
        num = "".join(change[x] for x in str(len(num)))
        sol.append(num)
    return sol
