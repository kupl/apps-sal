three_details=lambda n:(lambda l:min(n%2**l,-n%2**l))(int(__import__('math').log2(n)))
