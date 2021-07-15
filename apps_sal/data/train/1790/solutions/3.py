class Graph():

    def __init__(self, vertices_num):
        # number of nodes (an integer)
        self.v = vertices_num
        # (maybe not useful here) : list of nodes from "A0", "A1" ... to "A index (vertices_num - 1)"
        self.nodes = None

    # from adjacency matrix to dictionary
    def adjmat_2_graph(self, matrix):
        dictionary = {}
        step = 0
        for row in matrix:
            dictionary[f"A{step}"] = []
            column = 0
            for value in row:
                if value:
                    dictionary[f"A{step}"].append((f"A{column}", value))
                column += 1
            step += 1
        return dictionary
        
    # from dictionary to adjacency matrix
    def graph_2_mat(self, dictionary):
        matrix = []
        step = 0
        while step < len(dictionary):
            row = [0] * len(dictionary)
            for edge in dictionary[f"A{step}"]:
                row[int(edge[0][1])] = edge[1]
            matrix.append(row)
            step += 1
        return matrix
    
    # from dictionary to adjacency list    
    def graph_2_list(self, dictionary):
        list = []
        step = 0
        while step < len(dictionary):
            vertex = [f"A{step}", dictionary[f"A{step}"]]
            list.append(vertex)
            step += 1
        return list
        
    # from adjacency list to dictionary
    def list_2_graph(self, list):
        dictionary = {}
        for vertex in list:
            dictionary[vertex[0]] = vertex[1]
        return dictionary
        
    # from adjacency matrix to adjacency list    
    def mat_2_list(self, matrix):
        list = []
        step = 0
        for row in matrix:
            vertex = [f"A{step}", []]
            column = 0
            for value in row:
                if value:
                    vertex[1].append((f"A{column}", value))
                column += 1
            list.append(vertex)
            step += 1
        return list
    
    # from adjacency list to adjacency matrix
    def list_2_mat(self, list):
        matrix = []
        step = 0
        while step < len(list):
            for vertex in list:
                if vertex[0] == f"A{step}":
                    row = [0] * len(list)
                    for edge in vertex[1]:
                        row[int(edge[0][1])] = edge[1]
                    matrix.append(row)
                    step += 1
        return matrix
        
    # find all path from node start_vertex to node end_vertex
    def find_all_paths(self, dictionary, start, end):
        def dfs(dictionary, start, end, path = []):
            path = path + [start]
            if start == end:
                return [path]
            if start not in dictionary:
                return []
            paths = []
            for edge in dictionary[start]:
                if edge[0] not in path:
                    newpaths = dfs(dictionary, edge[0], end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            return paths
        paths = dfs(dictionary, start, end)
        return sorted(sorted(["-".join(path) for path in paths], key = str), key = len)
        

