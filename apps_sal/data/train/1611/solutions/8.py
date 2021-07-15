UPPER_BOUND = 1000000000

def test_call (current_function: str, functions: dict, stack: set):
    min_n = UPPER_BOUND
    max_n = 0

    stack.add(current_function)
    #print("    " * len(stack), current_function, ' ', functions,
    #        current_function in stack, sep='')
    for next_funcion in functions[current_function]:
        if next_funcion in stack:
            min_n = min(min_n, 1)
            max_n = max(max_n, 1)

        else:
            current_min, current_max = \
                    test_call(next_funcion, functions, stack)
            current_min += 1
            current_max += 1
            if current_min < min_n:
                min_n = current_min
            if current_min == 1:
                min_n = 0
            if current_max != 1 and current_max > max_n:
                max_n = current_max
    stack.remove(current_function)
    if min_n == UPPER_BOUND:
        min_n = 0
    if max_n < min_n:
        max_n = min_n
    return (min_n, max_n)

def read_function(s: str):
    """
    return:
        (function_#, [functions called])
    """
    i = 0;
    while (s[i] in "0123456789"):
        i += 1

    function_no = int(s[0:i])
    function_calls = []

    #print("Reading", function_no)

    while 1:
        i = s.find('P', i)
        if i < 0:
            break;
        nums = i + 1
        i += 1
        while i < len(s) and s[i] in "0123456789":
            i += 1
        nume = i
        #print("    call from", nums, "to", nume)
        function_call = int(s[nums:nume])
        function_calls.append(function_call)

    return (function_no, function_calls)

def parse_program (program_s: str):
    i = 0;
    functions = {}

    while 1:
        i = program_s.find('p', i)
        if i < 0:
            break
        funs = i + 1
        i = program_s.find('q', i)
        fune = i
        func_no, fun_calls = read_function(program_s[funs:fune])
        functions[func_no] = fun_calls


    #print("Finish parsing")
    i = 0;
    min_n, max_n = UPPER_BOUND, 0

    while 1:
        next_sof = program_s.find('p', i)
        next_eof = program_s.find('q', i)
        if (next_sof < 0):
            next_sof = len(program_s)

        #print("WTF", next_sof, next_eof)

        while 1:
            i = program_s.find('P', i)
            if i < 0 or i >= next_sof:
                break;
            nums = i + 1
            i += 1
            while i < len(program_s) and program_s[i] in "0123456789":
                i += 1
            nume = i
            #print("Calling", nums, nume)
            function_call = int(program_s[nums:nume])
            c_min_n, c_max_n = test_call(function_call, functions, set())
            if c_min_n < min_n:
                min_n = c_min_n
            if c_max_n > max_n:
                max_n = c_max_n

        if i < 0 or next_eof < 0:
            break
        i = next_eof + 1


    if min_n == UPPER_BOUND:
        min_n = 0
        max_n = 0

    return [min_n, max_n]


def magic_call_depth_number(pattern):
    return parse_program(pattern)



