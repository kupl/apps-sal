number_of_test_cases = int(input())

for i in range(0,number_of_test_cases):
    radius = int(input())
    area = 3.14 * radius * radius
    print(round(area,2))
