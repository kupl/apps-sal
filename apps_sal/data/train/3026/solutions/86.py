def min_value(digits):
    if len(digits) > 1:
        # Sort ascending order
        digits.sort()
        
        # Remove duplicats from list
        output = []
        counter = 1
        for i in digits:
            if i != digits[counter]:
                output.append(i)
            if counter != len(digits) - 1:
                counter += 1
        output.append(digits[-1])
            
        # Turn integers to string and join
        output = [str(i) for i in output]
        output =int(''.join(output))
        return output
    return digits[0]
    
    

