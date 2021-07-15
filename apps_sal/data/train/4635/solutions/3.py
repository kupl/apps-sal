def create_octahedron(size):
    if size<3 or size%2==0:
        return []
    result = []
    center = size//2
    for plane in range(size):
        inner = [[0 if abs(center-i)+abs(center-j)+abs(center-plane)>center else 1 for i in range(size)] for j in range(size)]
        result.append(inner)
    return result
