class Identifier:
     def __init__(self, name):
         self.name = name
 
     def __str__(self):
         return "{}".format(self.name)
 
 class Number:
     def __init__(self, value):
         self.value = value
 
     def __str__(self):
         return "{}".format(self.value)
 
 class Binary:
     def __init__(self, op, left, right):
         self.op = op
         self.left = left
         self.right = right
 
     def __str__(self):
         return "({} {} {})".format(self.left, self.op, self.right)
 
 class Solution:
     def basicCalculatorIV(self, expression, evalvars, evalints):
         """
         :type expression: str
         :type evalvars: List[str]
         :type evalints: List[int]
         :rtype: List[str]
         """
         variables = dict(zip(evalvars, evalints))
 
         def lex(string):
             output = []
             i = 0
             while i < len(string):
                 if string[i] == " ":
                     i += 1
                 elif string[i] in "()*+-":
                     output.append(string[i])
                     i += 1
                 elif string[i].islower():
                     j = i
                     while j < len(string) and string[j].islower():
                         j += 1
                     name = string[i:j]
                     output.append(Identifier(name))
                     i = j
                 elif string[i].isdigit():
                     j = i
                     while j < len(string) and string[j].isdigit():
                         j += 1
                     value = int(string[i:j])
                     output.append(Number(value))
                     i = j
                 else:
                     i += 1
             return output
 
         precedence = { "*" : 2, "+" : 1, "-" : 1 }
 
         def parse(tokens, p = 0):
             if not tokens:
                 return tokens, None
             elif tokens[0] == "(":
                 tokens = tokens[1:]
                 tokens, node = parse(tokens)
                 if tokens[0] != ")":
                     return tokens, None
                 tokens = tokens[1:]
             elif isinstance(tokens[0], Identifier):
                 name = tokens[0].name
                 if name in variables:
                     node = Number(variables[name])
                 else:
                     node = Identifier(name)
                 tokens = tokens[1:]
             elif isinstance(tokens[0], Number):
                 node = Number(tokens[0].value)
                 tokens = tokens[1:]
             while tokens and tokens[0] in precedence and precedence[tokens[0]] > p:
                 binary = tokens[0]
                 tokens, right = parse(tokens[1:], precedence[binary])
                 node = Binary(binary, node, right)
             return tokens, node
 
         def compare(a, b):
             if a is None or b is None:
                 return (b is None) - (a is None)
             cmp = len(a) - len(b)
             if cmp != 0:
                 return cmp
             a = " ".join(a)
             b = " ".join(b)
             return (a < b) - (a > b)
 
         def evaluate(ast):
             if isinstance(ast, Identifier):
                 return [(1, [ast.name])]
             elif isinstance(ast, Number):
                 return [(ast.value, [])] if ast.value != 0 else []
             elif isinstance(ast, Binary):
                 left = evaluate(ast.left)
                 right = evaluate(ast.right)
                 if ast.op == "*":
                     output = {}
                     for a in left:
                         for b in right:
                             value = sorted(a[1] + b[1])
                             key = " ".join(value)
                             if key not in output:
                                 output[key] = 0
                             output[key] += a[0] * b[0]
                             if output[key] == 0:
                                 del output[key]
 
                     class K:
                         def __init__(self, inner):
                             self.inner = inner[1]
                         
                         def __lt__(self, other):
                             return compare(self.inner, other.inner) > 0
 
                     return sorted(map(lambda x: (x[1], x[0].split()), output.items()), key=K)
                 elif ast.op in "+-":
                     output = []
                     left = iter(left)
                     right = iter(right)
                     a = next(left, None)
                     b = next(right, None)
                     while a or b:
                         result = compare(a and a[1], b and b[1])
                         if result > 0:
                             output.append(a)
                             a = next(left, None)
                         elif result < 0:
                             output.append(b if ast.op == "+" else (-b[0], b[1]))
                             b = next(right, None)
                         else:
                             coeff = a[0] + b[0] if ast.op == "+" else a[0] - b[0]
                             if coeff != 0:
                                 output.append((coeff, a[1]))
                             a = next(left, None)
                             b = next(right, None)
                     return output
                 else:
                     return None
             else:
                 return None
 
         def format(expression):
             return ["*".join([str(e[0])] + e[1]) for e in expression]
 
         tokens = lex(expression)
         _, ast = parse(tokens)
         expression = evaluate(ast)
         output = format(expression)
 
         return output
