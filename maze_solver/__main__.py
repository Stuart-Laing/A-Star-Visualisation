from maze_solver.generate_maze import read_maze
from maze_solver.draw import draw_border, draw_start_finish, draw_path, draw_node
from maze_solver.solve_maze import solve_maze

import turtle


turtle_object = turtle.Turtle()
window = turtle.Screen()

window.setup(1050, 550)
window.tracer(0, 0)
window.title("Maze Solver")
window.bgcolor("darkgray")

turtle_object.speed(0)
turtle_object.pensize(1)
turtle_object.hideturtle()
turtle_object.penup()

maze_array = read_maze("Demo-Mazes/maze-3.txt")

draw_border(turtle_object)

for row in range(0, 24):
    for col in range(0, 50):
        draw_node(turtle_object, col, row, maze_array[row][col])

start = (1, 2)
finish = (22, 20)

draw_start_finish(turtle_object, start[0], start[1], True)
draw_start_finish(turtle_object, finish[0], finish[1], False)

draw_path(turtle_object, solve_maze(maze_array, start, finish))

window.update()

window.listen()
window.mainloop()