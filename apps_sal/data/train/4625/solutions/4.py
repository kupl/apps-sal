from collections import defaultdict, namedtuple

Edge = namedtuple('Edge', ['process_name', 'to'])
State = namedtuple('State', ['stack', 'visited', 'min_stack'])

def dfs(graph, cur_node, end_node, state):
    if cur_node in state.visited:
        return
    if len(state.min_stack) and len(state.stack) >= len(state.min_stack):
        return
    if cur_node == end_node:
        state.min_stack.clear()
        state.min_stack.extend(state.stack)
        return

    state.visited.add(cur_node)
    for process, node in graph[cur_node]:
        state.stack.append(process)
        dfs(graph, node, end_node, state)
        state.stack.pop()
    state.visited.remove(cur_node)

def processes(start, end, processes):
  if start == end:
      return []
  graph = defaultdict(list)
  
  for process_name, start_node, end_node in processes:
      graph[start_node].append(Edge(process_name, end_node))
  
  state = State([], set(), [])
  dfs(graph, start, end, state)
  
  return state.min_stack
