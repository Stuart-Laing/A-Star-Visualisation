import draw_final_path


import turtle
import random


def draw_maze(maze_array):

    for x_index in range(0, 50):
        for y_index in range(0, 24):
            pass
            draw_square(x_index, y_index, maze_array[y_index][x_index])

    # <x>, <y> = <Top Left> : <Bottom Right>

    # 23, 11 = -20, 20
    # 24, 11 = 0, 20
    # 23, 12 = -20, 0
    # 24, 12 = 0, 0

    # 48x = -10 : (x - 49) * 10
    # 49x = 0 : (x - 49) * 10
    # 24y = 10 : (y - 25) * -10
    # 25y = 0 : (y - 25) * -10


def draw_square(x_index, y_index, color_value):
    turtle_object.setheading(0)

    colour = "#00" + hex(int(round(color_value * 255)))[2:].zfill(2) + "00"

    turtle_object.color(colour)
    turtle_object.fillcolor(colour)

    x_top_left = (x_index - 25) * 20
    y_top_left = (y_index - 12) * -20

    turtle_object.begin_fill()

    turtle_object.setposition(x_top_left, y_top_left)

    turtle_object.pendown()

    turtle_object.forward(19)
    turtle_object.right(90)

    turtle_object.forward(19)
    turtle_object.right(90)

    turtle_object.forward(19)
    turtle_object.right(90)

    turtle_object.forward(19)

    turtle_object.end_fill()

    turtle_object.penup()


def left_click(x, y):
    print(x, y)


def read_maze(path):
    with open(path, "r") as f:
        maze_array = [list(line.strip()) for line in f.readlines()]

    return maze_array


def draw_start_finish(coords, start):
    if coords[0] - coords[2] == -1:
        x_top_left = ((coords[0] - 25) * 20) + 16
        y_top_left = ((coords[1] - 12) * -20) - 6

    elif coords[0] - coords[2] == 1:
        x_top_left = ((coords[2] - 25) * 20) + 16
        y_top_left = ((coords[3] - 12) * -20) - 6

    elif coords[1] - coords[3] == -1:
        x_top_left = ((coords[0] - 25) * 20) + 6
        y_top_left = ((coords[1] - 12) * -20) - 16

    else:
        # elif coords[1] - coords[3] == 1:
        x_top_left = ((coords[2] - 25) * 20) + 6
        y_top_left = ((coords[3] - 12) * -20) - 16

    turtle_object.setheading(0)

    turtle_object.color("yellow")
    if start:
        turtle_object.fillcolor("blue")

    else:
        turtle_object.fillcolor("purple")

    turtle_object.begin_fill()

    turtle_object.penup()
    turtle_object.setposition(x_top_left, y_top_left)
    turtle_object.pendown()

    turtle_object.forward(7)
    turtle_object.right(90)

    turtle_object.forward(7)
    turtle_object.right(90)

    turtle_object.forward(7)
    turtle_object.right(90)

    turtle_object.forward(7)

    turtle_object.end_fill()

    turtle_object.penup()


def draw_border():
    turtle_object.setheading(0)
    turtle_object.color("blue")
    turtle_object.setposition(-503, 243)

    turtle_object.pendown()

    line_lengths = (1005, 485, 1005, 484, 1004, 483, 1003, 482, 1002, 481, 1001, 481)
    for length in line_lengths:
        turtle_object.forward(length)
        turtle_object.right(90)

    turtle_object.penup()


def random_sub_point():
    random_x = random.randint(1, 48)
    random_y = random.randint(1, 22)

    if random.random() > 0.5:
        sub_point = (random_x, random_y, random_x + (1 if random.random() > 0.5 else -1), random_y)
    else:
        sub_point = (random_x, random_y, random_x, random_y + (1 if random.random() > 0.5 else -1))

    return sub_point


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
    draw_final_path.draw_path(turtle_object,
                              [(20, 1), (21, 1), (21, 2), (21, 3), (20, 3), (19, 3), (18, 3),
                               (17, 3), (16, 3), (15, 3), (15, 2), (15, 1), (16, 1)])

    # start = (0, 0, 0, 0)
    # finish = (0, 0, 0, 0)
    #
    # while start == finish:
    #     start = random_sub_point()
    #     finish = random_sub_point()
    #
    # print(f"Start Point: {start}")
    # print(f"End Point: {finish}")
    #
    # draw_start_finish(start, True)
    # draw_start_finish(finish, False)

    draw_start_finish((16, 1, 17, 1), True)
    draw_start_finish((19, 1, 20, 1), False)

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
