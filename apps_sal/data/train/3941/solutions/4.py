def reverse_fizzbuzz(fizzbuzz_section):
    fizzbuzz_section_elements = fizzbuzz_section.split()
    n = len(fizzbuzz_section_elements)
    
    for index in range(0, n):
        if fizzbuzz_section_elements[index].isdigit():
            start = int(fizzbuzz_section_elements[index]) - index
            return list(range(start, n + start))
    
    fizzbuzz = {
        'Fizz': [3], 
        'Buzz': [5], 
        'FizzBuzz': [15], 
        'Fizz Buzz': [9, 10], 
        'Buzz Fizz': [5, 6]
    }
    
    return fizzbuzz[fizzbuzz_section]
