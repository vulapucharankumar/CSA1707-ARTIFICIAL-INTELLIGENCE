class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.position = (0, 0)  # Initial position of the vacuum cleaner

    def print_grid(self):
        for row in self.grid:
            print(" ".join(row))
        print()

    def is_dirty(self, position):
        return self.grid[position[0]][position[1]] == 'D'

    def clean(self, position):
        self.grid[position[0]][position[1]] = '-'

    def move_left(self):
        self.position = (self.position[0], max(0, self.position[1] - 1))

    def move_right(self):
        self.position = (self.position[0], min(len(self.grid[0]) - 1, self.position[1] + 1))

    def move_up(self):
        self.position = (max(0, self.position[0] - 1), self.position[1])

    def move_down(self):
        self.position = (min(len(self.grid) - 1, self.position[0] + 1), self.position[1])

    def clean_environment(self):
        while any('D' in row for row in self.grid):
            self.print_grid()
            if self.is_dirty(self.position):
                print(f"Cleaning {self.position}")
                self.clean(self.position)
            else:
                print(f"Moving to {self.position}")

            # Move to the next dirty cell
            if any('D' in row for row in self.grid):
                if self.position[1] < len(self.grid[0]) - 1 and 'D' in self.grid[self.position[0]]:
                    self.move_right()
                elif self.position[0] < len(self.grid) - 1 and 'D' in [row[self.position[1]] for row in self.grid]:
                    self.move_down()
                elif self.position[1] > 0 and 'D' in self.grid[self.position[0]]:
                    self.move_left()
                elif self.position[0] > 0 and 'D' in [row[self.position[1]] for row in self.grid]:
                    self.move_up()


# Example usage:
if __name__ == "__main__":
    # Define the environment grid (D represents dirty cells)
    grid = [
        ['D', '-', 'D', '-'],
        ['-', 'D', '-', 'D'],
        ['D', '-', '-', '-']
    ]

    vacuum_cleaner = VacuumCleaner(grid)
    vacuum_cleaner.clean_environment()
