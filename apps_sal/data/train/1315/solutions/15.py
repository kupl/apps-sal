# cook your dish here
from collections import Counter

quiz_set = []

for question_set in range(int(input())):
    qs = tuple(sorted(map(int, input().split())))
    quiz_set.append(qs)

# print(quiz_set)
quiz_set = Counter(quiz_set)
# print(quiz_set)

unique_counts = list(quiz_set.values()).count(1)

print(unique_counts)
