# cook your dish here
class TestCase:
    def __init__(self):
        [self.node_count, self.query_count] = read_line()
        
    def fill_nodes(self):
        self.nodes = {n+1: [] for n in range(self.node_count)}
        for i in range(self.node_count -1):
            new_node_1, new_node_2 = read_line()
            self.nodes[new_node_1].append(new_node_2)
            self.nodes[new_node_2].append(new_node_1)
            
    def resolve_query(self, query):
        a, d_a, b, d_b = query
        suiting_a = self.find_nodes_with_distance(a, d_a)
        suiting_b = self.find_nodes_with_distance(b, d_b)
        fitting = [node for node in suiting_a if node in suiting_b]
        
        if len(fitting) == 0:
            return -1
        else:
            return fitting[0]
        
    def find_nodes_with_distance(self, start_node, distance):
        from_nodes = {start_node}
        passed_nodes = from_nodes
        
        for i in range(distance):
            to_nodes = set()
            # add all adjacent nodes
            for node in from_nodes:
                to_nodes.update(self.nodes[node])
            
            # no backtracking
            for node in passed_nodes:
                if node in to_nodes:
                    to_nodes.remove(node)
            
            # update which nodes are passed
            passed_nodes.update(to_nodes)
            # go another round with the new nodes found
            from_nodes = to_nodes
        return list(from_nodes)

def read_line():
    line = input()
    return [int(s) for s in line.split(' ')]

num_testcases = int(input())
for i in range(num_testcases):
    testcase = TestCase()
    testcase.fill_nodes()
    for q in range(testcase.query_count):
        query = read_line()
        print(testcase.resolve_query(query))
