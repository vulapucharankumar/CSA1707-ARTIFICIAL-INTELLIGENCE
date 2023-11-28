import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic estimate from current node to goal node

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def astar(start_state, goal_state, neighbors_func, heuristic_func):
    start_node = Node(state=start_state, g=0, h=heuristic_func(start_state))
    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor_state in neighbors_func(current_node.state):
            if neighbor_state in closed_set:
                continue

            neighbor_g = current_node.g + 1
            neighbor_h = heuristic_func(neighbor_state)
            neighbor_node = Node(state=neighbor_state, parent=current_node, g=neighbor_g, h=neighbor_h)

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

    return None  # No path found

# Example usage:
def neighbors(state):
    x, y = state
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]  # Adjacent cells

def heuristic(state):
    goal_state = (5, 5)  # Example goal state
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])  # Manhattan distance

start_state = (0, 0)
goal_state = (5, 5)

result = astar(start_state, goal_state, neighbors, heuristic)
if result:
    print("Path found:", result)
else:
    print("No path found.")
