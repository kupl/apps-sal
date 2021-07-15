from re import findall;trump_detector=lambda t: round(sum(map(lambda a: len(a[1]), findall(r"([aeiou])(\1*)",t,2)))/len(findall(r"([aeiou])(\1*)",t,2)),2)
