from queue import Queue

def water_jug_problem(capacity_a, capacity_b, target):
    visited_states = set()
    initial_state = (0, 0)

    queue = Queue()
    queue.put(initial_state)
    visited_states.add(initial_state)

    while not queue.empty():
        current_state = queue.get()
        jug_a, jug_b = current_state

        if jug_a == target or jug_b == target:
            print("Solution found:", current_state)
            return

        # Fill jug A
        next_state = (capacity_a, jug_b)
        if next_state not in visited_states:
            queue.put(next_state)
            visited_states.add(next_state)

        # Fill jug B
        next_state = (jug_a, capacity_b)
        if next_state not in visited_states:
            queue.put(next_state)
            visited_states.add(next_state)

        # Empty jug A
        next_state = (0, jug_b)
        if next_state not in visited_states:
            queue.put(next_state)
            visited_states.add(next_state)

        # Empty jug B
        next_state = (jug_a, 0)
        if next_state not in visited_states:
            queue.put(next_state)
            visited_states.add(next_state)

        # Pour water from jug A to jug B
        pour_amount = min(jug_a, capacity_b - jug_b)
        next_state = (jug_a - pour_amount, jug_b + pour_amount)
        if next_state not in visited_states:
            queue.put(next_state)
            visited_states.add(next_state)

        # Pour water from jug B to jug A
        pour_amount = min(jug_b, capacity_a - jug_a)
        next_state = (jug_a + pour_amount, jug_b - pour_amount)
        if next_state not in visited_states:
            queue.put(next_state)
            visited_states.add(next_state)

    print("Solution not found")

# Example usage:
water_jug_problem(4, 3, 2)
