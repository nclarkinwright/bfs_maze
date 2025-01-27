# Nicholas Clarkin-Wright
# nc819094@wcupa.edu
# HW 1

import time

class Maze():
    """A pathfinding problem."""

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location
    
    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('*', end=' ')
                else:
                    print(self.grid[r][c], end=' ')
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        # Grid goes (y, x)
        possible_moves = []

        # Check north
        if self.grid[self.location[0] - 1][self.location[1]] == ' ':
            possible_moves.append('N')
        # Check south
        if self.grid[self.location[0] + 1][self.location[1]] == ' ':
            possible_moves.append('S')
        # Check east
        if self.grid[self.location[0]][self.location[1] + 1] == ' ':
            possible_moves.append('E')
        # Check west
        if self.grid[self.location[0]][self.location[1] - 1] == ' ':
            possible_moves.append('W')

        return possible_moves

    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        # Grid goes (y, x)
        moved = Maze(self.grid, self.location)

        # Move north
        if (move == 'N'):
            moved.location = (moved.location[0] - 1, moved.location[1])
        # Move east
        if (move == 'E'):
            moved.location = (moved.location[0], moved.location[1] + 1)
        # Move south
        if (move == 'S'):
            moved.location = (moved.location[0] + 1, moved.location[1])
        # Move west
        if (move == 'W'):
            moved.location = (moved.location[0], moved.location[1] - 1)
        
        return moved
    
    def has_same_location (self, maze):
        return self.location == maze.location

class Agent():
    """Knows how to find the exit to a maze with BFS."""

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        start = maze.location
        frontier = [start]
        explored = {start: (start, ' ')}
        goal_found = False

        while frontier != [] and not(goal_found):
            parent = frontier.pop()
            parent_maze = Maze(maze.grid, parent)
            children = parent_maze.moves()
            for x in children:
                child_maze = parent_maze.neighbor(x)
                if child_maze.location not in explored:
                    explored.setdefault(child_maze.location, (parent, x))
                    frontier.append(child_maze.location)
                    if child_maze.has_same_location(goal):
                        goal_found = True
                        break
        
        return find_path(maze, goal, explored)

# Finds shortest path from start to goal from explored dictionary from the bfs function
def find_path(maze, goal, explored):
    path = []
    child = goal.location
    parent_and_direction = explored.get(child)
    parent = parent_and_direction[0]
    direction = parent_and_direction[1]
    path.append(direction) 
    
    while (child != parent):
        child = parent
        parent_and_direction = explored.get(child)
        parent = parent_and_direction[0]
        direction = parent_and_direction[1]
        if (direction != ' '):
            path.append(direction)

    return path[::-1]

def main():
    """Create a maze, solve it with BFS, and console-animate."""
    

grid = ["XXXXXXXXXXXXXXXXXXXX",
        "X     X    X       X",
        "X XXXXX XXXX XXX XXX",
        "X       X      X X X",
        "X X XXX XXXXXX X X X",
        "X X   X        X X X",
        "X XXX XXXXXX XXXXX X",
        "X XXX    X X X     X",
        "X    XXX       XXXXX",
        "XXXXX   XXXXXX     X",
        "X   XXX X X    X X X",
        "XXX XXX X X XXXX X X",
        "X     X X   XX X X X",
        "XXXXX     XXXX X XXX",
        "X     X XXX    X   X",
        "X XXXXX X XXXX XXX X",
        "X X     X  X X     X",
        "X X XXXXXX X XXXXX X",
        "X X                X",
        "XXXXXXXXXXXXXXXXXX X"]

maze = Maze(grid, (1, 1))
maze.display()

agent = Agent()
goal = Maze(grid, (19, 18))
path = agent.bfs(maze, goal)

while path:
    move = path.pop(0)
    maze = maze.neighbor(move)
    time.sleep(0.25)
    maze.display()

if __name__ == '__main__':
    main()