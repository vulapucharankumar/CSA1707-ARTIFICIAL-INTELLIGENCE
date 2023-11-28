from itertools import permutations

def calculate_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i + 1]]
    total_distance += distances[order[-1]][order[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    min_distance = float('inf')
    optimal_route = None

    for perm in permutations(cities):
        distance = calculate_distance(perm, distances)
        if distance < min_distance:
            min_distance = distance
            optimal_route = perm

    return optimal_route, min_distance

# Example usage
if __name__ == "__main__":
    # Example distance matrix (replace this with your actual data)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    optimal_route, min_distance = traveling_salesman_bruteforce(distance_matrix)

    print("Optimal Route:", optimal_route)
    print("Minimum Distance:", min_distance)
