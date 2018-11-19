import random

class Cell:
    def __init__(self):
        self.current_generation = random.randint(0,1)
        self.next_generation = 0
    
    def evolve(self):
        self.current_generation = self.next_generation
        self.next_generation = 0

    def is_live(self):
        return self.current_generation

    def __str__(self):
        return str(self.current_generation)

class World:
    def __init__(self, size):
        self.size = size
        self.grid = [[Cell() for x in range(size)] for x in range(size)]
    
    def make_next_generation(self):
        for x in range(self.size):
            for y in range(self.size):
                self.run_rules(x, y)
        self.apply_rules()
    
    def apply_rules(self):
        for x in range(self.size):
            for y in range(self.size):
                self.grid[x][y].evolve()

    def run_rules(self, x, y):
        live_neighbors = self.get_live_neighbors(x, y)
        if self.grid[x][y].is_live():
            if live_neighbors < 2:
                self.grid[x][y].next_generation = 0
            elif 2 <= live_neighbors <= 3:
                self.grid[x][y].next_generation = 1
            elif live_neighbors > 3:
                self.grid[x][y].next_generation = 0
        else:
            if live_neighbors == 3:
                self.grid[x][y].next_generation = 1

    def get_live_neighbors(self, x, y):
        live_neighbors = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if self.are_valid_indices(i,j) and (i,j) != (x,y):
                    live_neighbors += 1 if self.grid[i][j].current_generation == 1 else 0
        return live_neighbors

    def are_valid_indices(self, i, j):
        return ((i >= 0 and i <= self.size-1) and (j >= 0 and j <= self.size-1))

    def __str__(self):
        lines = ""
        for x in range(self.size):
            for y in range(self.size):
                lines += str(self.grid[x][y])
            lines += "\n"
        return lines

if __name__ == "__main__":
    SIZE = 15
    world = World(SIZE)
    while(True):
        print(world)
        world.make_next_generation()
        input("Press Enter for next Generation...")