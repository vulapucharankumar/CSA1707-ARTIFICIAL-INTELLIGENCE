from queue import Queue

# State representation: (left_bank_m, left_bank_c, boat, right_bank_m, right_bank_c)
# where m = missionaries, c = cannibals, boat = 0 or 1 (0 for left, 1 for right)

def is_valid_state(state):
    left_m, left_c, boat, right_m, right_c = state
    return (left_m >= 0 and left_c >= 0 and right_m >= 0 and right_c >= 0
            and (left_m == 0 or left_m >= left_c) and (right_m == 0 or right_m >= right_c))

def is_goal_state(state):
    return state == (0, 0, 0, 3, 3)

def get_next_states(current_state):
    left_m, left_c, boat, right_m, right_c = current_state
    possible_moves = []
    
    if boat == 0:  # Boat on the left side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (left_m - m, left_c - c, 1, right_m + m, right_c + c)
                    if is_valid_state(new_state):
                        possible_moves.append(new_state)
    else:  # Boat on the right side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (left_m + m, left_c + c, 0, right_m - m, right_c - c)
                    if is_valid_state(new_state):
                        possible_moves.append(new_state)
    
    return possible_moves

def solve():
    initial_state = (3, 3, 0, 0, 0)
    goal_state = (0, 0, 0, 3, 3)
    
    visited = set()
    q = Queue()
    q.put(initial_state)
    visited.add(initial_state)
    
    while not q.empty():
        current_state = q.get()
        
        if is_goal_state(current_state):
            return current_state
        
        next_states = get_next_states(current_state)
        
        for next_state in next_states:
            if next_state not in visited:
                q.put(next_state)
                visited.add(next_state)
    
    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        print("Missionaries and Cannibals problem solution:")
        print("Initial state: (3M, 3C, B, 0M, 0C)")
        for state in solution:
            print(f"Move the boat to {'right' if state[2] == 1 else 'left'}: ({state[0]}M, {state[1]}C, B, {state[3]}M, {state[4]}C)")

if __name__ == "__main__":
    solution = solve()
    print_solution(solution)
from queue import Queue

# State representation: (left_bank_m, left_bank_c, boat, right_bank_m, right_bank_c)
# where m = missionaries, c = cannibals, boat = 0 or 1 (0 for left, 1 for right)

def is_valid_state(state):
    left_m, left_c, boat, right_m, right_c = state
    return (left_m >= 0 and left_c >= 0 and right_m >= 0 and right_c >= 0
            and (left_m == 0 or left_m >= left_c) and (right_m == 0 or right_m >= right_c))

def is_goal_state(state):
    return state == (0, 0, 0, 3, 3)

def get_next_states(current_state):
    left_m, left_c, boat, right_m, right_c = current_state
    possible_moves = []
    
    if boat == 0:  # Boat on the left side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (left_m - m, left_c - c, 1, right_m + m, right_c + c)
                    if is_valid_state(new_state):
                        possible_moves.append(new_state)
    else:  # Boat on the right side
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (left_m + m, left_c + c, 0, right_m - m, right_c - c)
                    if is_valid_state(new_state):
                        possible_moves.append(new_state)
    
    return possible_moves

def solve():
    initial_state = (3, 3, 0, 0, 0)
    goal_state = (0, 0, 0, 3, 3)
    
    visited = set()
    q = Queue()
    q.put(initial_state)
    visited.add(initial_state)
    
    while not q.empty():
        current_state = q.get()
        
        if is_goal_state(current_state):
            return current_state
        
        next_states = get_next_states(current_state)
        
        for next_state in next_states:
            if next_state not in visited:
                q.put(next_state)
                visited.add(next_state)
    
    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        print("Missionaries and Cannibals problem solution:")
        print("Initial state: (3M, 3C, B, 0M, 0C)")
        for state in solution:
            print(f"Move the boat to {'right' if state[2] == 1 else 'left'}: ({state[0]}M, {state[1]}C, B, {state[3]}M, {state[4]}C)")

if __name__ == "__main__":
    solution = solve()
    print_solution(solution)
