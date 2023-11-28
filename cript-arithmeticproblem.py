from itertools import permutations

def is_valid(puzzle, solution):
    # Check if the solution satisfies the puzzle
    puzzle_letters = set(''.join(puzzle))
    solution_letters = set(solution.keys())
    
    if len(puzzle_letters) != len(solution_letters):
        return False

    for word in puzzle:
        if word[0] in solution:
            if solution[word[0]] == '0':
                return False

    left_operand = ''.join(solution[c] for c in puzzle[0])
    right_operand = ''.join(solution[c] for c in puzzle[2])
    result = ''.join(solution[c] for c in puzzle[4])

    return int(left_operand) + int(right_operand) == int(result)

def solve_cryptarithmetic(puzzle):
    # Extract unique letters from the puzzle
    letters = set(''.join(puzzle))

    # Generate all possible permutations of digits from 0 to 9 for the letters
    for perm in permutations("0123456789", len(letters)):
        solution = dict(zip(letters, perm))
        
        if is_valid(puzzle, solution):
            return solution

    return None

if __name__ == "__main__":
    # Example cryptarithmetic puzzle: SEND + MORE = MONEY
    puzzle = ["SEND", "MORE", "MONEY"]

    solution = solve_cryptarithmetic(puzzle)

    if solution:
        print("Solution found:")
        for word in puzzle:
            print(''.join(solution[c] for c in word), end=" ")
    else:
        print("No solution found.")
