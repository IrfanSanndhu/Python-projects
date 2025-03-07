from collections import deque

def find_diamond(maze, start):
    rows, cols = len(maze), len(maze[0])
    
    # Possible movement directions
    directions = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1)
    }

    queue = deque([(start, [])])  # (current position, path taken)
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        if maze[x][y] == 'D':  # Found diamond
            return path

        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if maze[nx][ny] != 'W':  # Avoid walls
                    queue.append(((nx, ny), path + [move]))
                    visited.add((nx, ny))

    return None  # No path found

# Define the maze
maze_map = [
    ['S', 'P', 'P', 'W'],
    ['P', 'W', 'P', 'P'],
    ['P', 'P', 'W', 'P'],
    ['W', 'D', 'W', 'W']
]

# Start position (0,0)
start_pos = (0, 0)

# Find shortest path
path_to_diamond = find_diamond(maze_map, start_pos)
print("Shortest Path:", path_to_diamond)