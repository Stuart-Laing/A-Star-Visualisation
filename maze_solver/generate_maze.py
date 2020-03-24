

def read_maze(path):
    with open(path, "r") as f:
        maze_array = [list(line.strip()) for line in f.readlines()]

    for row in range(0, len(maze_array)):
        for col in range(0, len(maze_array[0])):
            maze_array[row][col] = int(maze_array[row][col])

    return maze_array
