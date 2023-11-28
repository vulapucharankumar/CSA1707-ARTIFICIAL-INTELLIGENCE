import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __eq__(self, other):
        return self.state == other.state

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        total_distance = 0
        goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    goal_position = divmod(value - 1, 3)
                    total_distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
        return total_distance

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_moves(i, j):
    moves = []
    if i > 0:
        moves.append((-1, 0))
    if i < 2:
        moves.append((1, 0))
    if j > 0:
        moves.append((0, -1))
    if j < 2:
        moves.append((0, 1))
    return moves

def apply_move(state, move):
    i, j = get_blank_position(state)
    new_state = [row.copy() for row in state]
    new_i, new_j = i + move[0], j + move[1]
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state

def is_goal_state(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def solve_puzzle(initial_state):
    open_set = [PuzzleNode(initial_state)]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if is_goal_state(current_node.state):
            # Goal state found, reconstruct the path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(tuple(map(tuple, current_node.state)))

        i, j = get_blank_position(current_node.state)
        possible_moves = generate_moves(i, j)

        for move in possible_moves:
            new_state = apply_move(current_node.state, move)
            if tuple(map(tuple, new_state)) not in closed_set:
                new_node = PuzzleNode(new_state, current_node, move, current_node.cost + 1)
                heapq.heappush(open_set, new_node)

    return None  # No solution found

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    solution = solve_puzzle(initial_state)

    if solution:
        print("Solution:")
        for step, state in enumerate(solution):
            print(f"Step {step + 1}:")
            for row in state:
                print(row)
            print()
    else:
        print("No solution found.")
