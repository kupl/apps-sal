def array_leaders(numbers):
        return [element for index, element in enumerate(numbers) if element>sum(numbers[index+1::])]
