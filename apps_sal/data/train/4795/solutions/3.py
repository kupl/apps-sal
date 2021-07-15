from re import findall
flesch_kincaid=lambda text: round(len(text.split(" "))*0.39/len(findall("[.!?]",text))+len(findall("[AEIOUaeiou]+",text))*11.8/len(text.split(" "))-15.59,2)
