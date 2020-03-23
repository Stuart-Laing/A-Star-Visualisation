import turtle
import random


def draw_maze(maze_array):

    for x_index in range(0, 100):
        for y_index in range(0, 50):
            draw_square(x_index, y_index, maze_array[y_index][x_index])

    # <x>, <y> = <Top Left> : <Bottom Right>

    # 48, 24 = -10, 10
    # 49, 24 = 0, 10
    # 48, 25 = -10, 0
    # 49, 25 = 0, 0

    # 48x = -10 : (x - 49) * 10
    # 49x = 0 : (x - 49) * 10
    # 24y = 10 : (y - 25) * -10
    # 25y = 0 : (y - 25) * -10


def draw_square(x_index, y_index, color_value):
    turtle_object.setheading(0)

    colour = "#00" + hex(int(round(color_value * 255)))[2:].zfill(2) + "00"

    turtle_object.color(colour)
    turtle_object.fillcolor(colour)

    x_top_left = (x_index - 50) * 10
    y_top_left = (y_index - 25) * -10

    turtle_object.begin_fill()

    turtle_object.setposition(x_top_left, y_top_left)

    turtle_object.pendown()

    turtle_object.forward(9)
    turtle_object.right(90)

    turtle_object.forward(9)
    turtle_object.right(90)

    turtle_object.forward(9)
    turtle_object.right(90)

    turtle_object.forward(9)

    turtle_object.end_fill()

    turtle_object.penup()


def draw_path(path):
    for t in path:
        draw_path_square(t[0], t[1], "left->bottom")


def draw_path_square(x_index, y_index, square_type):
    x_top_left = (x_index - 50) * 10
    y_top_left = (y_index - 25) * -10




    #
    # if square_type == "left->right":
    #     turtle_object.setheading(0)
    #     turtle_object.color("red")
    #
    #     y_offsets = (0, 1, 8, 9)
    #     for offset in y_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left, y_top_left - offset)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(10)
    #
    # elif square_type == "left->top":
    #     turtle_object.setheading(0)
    #     turtle_object.color("red")
    #
    #     y_offsets = (8, 9)
    #     for offset in y_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left, y_top_left - offset)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(10)
    #
    #     turtle_object.setheading(-90)
    #     x_offsets = (8, 9)
    #     for offset in x_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left + offset, y_top_left)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(10)
    #
    #     x_offsets = (0, 1)
    #     for offset in x_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left + offset, y_top_left)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(2)
    #
    # elif square_type == "left->bottom":
    #     turtle_object.setheading(0)
    #     turtle_object.color("red")
    #
    #     y_offsets = (0, 1)
    #     for offset in y_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left, y_top_left - offset)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(10)
    #
    #     turtle_object.setheading(-90)
    #     x_offsets = (8, 9)
    #     for offset in x_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left + offset, y_top_left)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(10)
    #
    #     x_offsets = (0, 1)
    #     for offset in x_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left + offset, y_top_left - 8)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(2)
    #
    # elif square_type == "top->right":
    #     turtle_object.setheading(0)
    #     turtle_object.color("red")
    #
    #     y_offsets = (0, 1)
    #     for offset in y_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left, y_top_left - offset)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(10)
    #
    #     turtle_object.setheading(-90)
    #     x_offsets = (8, 9)
    #     for offset in x_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left + offset, y_top_left)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(10)
    #
    #     x_offsets = (0, 1)
    #     for offset in x_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left + offset, y_top_left - 8)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(2)
    #
    # elif square_type == "top->bottom":
    #     turtle_object.setheading(-90)
    #     turtle_object.color("red")
    #
    #     x_offsets = (0, 1, 8, 9)
    #     for offset in x_offsets:
    #         turtle_object.penup()
    #         turtle_object.setposition(x_top_left + offset, y_top_left)
    #         turtle_object.pendown()
    #
    #         turtle_object.forward(10)
    #
    # elif square_type == "bottom->right":
    #     pass

    # turtle_object.setheading(0)
    # turtle_object.color("red")
    #
    # # line_lengths = (9, 9, 9, 8, 8, 7, 7, 7)
    # # for length in line_lengths:
    # #     turtle_object.forward(length)
    # #     turtle_object.right(90)
    #
    # turtle_object.setposition((x_index - 50) * 10, (y_index - 25) * -10)
    # turtle_object.pendown()
    # turtle_object.forward(10)
    # turtle_object.penup()
    #
    # turtle_object.setposition((x_index - 50) * 10, (y_index - 25) * -10 - 1)
    # turtle_object.pendown()
    # turtle_object.forward(10)
    # turtle_object.penup()
    #
    # turtle_object.setposition((x_index - 50) * 10, (y_index - 25) * -10 - 8)
    # turtle_object.pendown()
    # turtle_object.forward(10)
    # turtle_object.penup()
    #
    # turtle_object.setposition((x_index - 50) * 10, (y_index - 25) * -10 - 9)
    # turtle_object.pendown()
    # turtle_object.forward(10)
    # turtle_object.penup()


def left_click(x, y):
    print(x, y)


def read_maze(path):
    with open(path, "r") as f:
        maze_array = [list(line.strip()) for line in f.readlines()]

    return maze_array


def draw_border():
    turtle_object.setheading(0)
    turtle_object.color("blue")
    turtle_object.setposition(-503, 253)

    turtle_object.pendown()

    line_lengths = (1005, 505, 1005, 504, 1004, 503, 1003, 502, 1002, 501, 1001, 501)
    for length in line_lengths:
        turtle_object.forward(length)
        turtle_object.right(90)

    turtle_object.penup()


def main():
    window.setup(1050, 550)
    window.tracer(0, 0)
    window.title("Path Finder")
    window.bgcolor("darkgray")

    turtle_object.speed(0)
    turtle_object.pensize(1)
    turtle_object.hideturtle()
    turtle_object.penup()

    maze_array = [[random.uniform(0.3, 1) for _ in range(0, 100)] for __ in range(0, 50)]
    # maze_array = [[str(random.randint(0, 1)) for _ in range(0, 100)] for __ in range(0, 50)]
    # maze_array = read_maze("maze.txt")

    draw_border()
    draw_maze(maze_array)
    draw_path([(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (3, 1), (3, 0)])

    window.update()

    window.onscreenclick(left_click, btn=1)
    # window.onscreenclick(middle_click, btn=2)
    # window.onscreenclick(right_click, btn=3)

    # window.onkey(w_key, key="w")

    window.listen()
    window.mainloop()


if __name__ == "__main__":
    turtle_object = turtle.Turtle()
    window = turtle.Screen()
    # game_board = GameBoard()
    main()
