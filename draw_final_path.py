

def draw_curve(turtle_object, x_start, y_start, start_heading):
    turtle_object.setheading(start_heading)

    turtle_object.penup()
    turtle_object.setposition(x_start, y_start)
    turtle_object.pendown()

    turtle_object.fillcolor("red")

    turtle_object.begin_fill()

    turtle_object.forward(19)
    turtle_object.left(90)

    turtle_object.forward(19)
    turtle_object.left(90)

    turtle_object.forward(3)
    turtle_object.left(90)

    turtle_object.forward(16)
    turtle_object.right(90)

    turtle_object.forward(16)
    turtle_object.left(90)

    turtle_object.forward(3)

    turtle_object.end_fill()


def draw_end(turtle_object, x_start, y_start, start_heading):
    turtle_object.setheading(start_heading)

    turtle_object.penup()
    turtle_object.setposition(x_start, y_start)
    turtle_object.pendown()

    turtle_object.fillcolor("red")

    turtle_object.begin_fill()

    turtle_object.forward(19)
    turtle_object.left(90)

    turtle_object.forward(19)
    turtle_object.left(90)

    turtle_object.forward(19)
    turtle_object.left(90)

    turtle_object.forward(3)
    turtle_object.left(90)

    turtle_object.forward(16)
    turtle_object.right(90)

    turtle_object.forward(13)
    turtle_object.right(90)

    turtle_object.forward(16)
    turtle_object.left(90)

    turtle_object.forward(3)

    turtle_object.end_fill()


def draw_square(turtle_object, x_start, y_start):
    turtle_object.setheading(0)

    turtle_object.penup()
    turtle_object.setposition(x_start, y_start)
    turtle_object.pendown()

    turtle_object.fillcolor("red")

    turtle_object.begin_fill()
    for i in range(0, 4):
        turtle_object.forward(3)
        turtle_object.right(90)
    turtle_object.end_fill()


def draw_line(turtle_object, x_start, y_start, start_heading):
    turtle_object.setheading(start_heading)

    turtle_object.penup()
    turtle_object.setposition(x_start, y_start)
    turtle_object.pendown()

    turtle_object.forward(20)


def draw_left_right(turtle_object, x_top_left, y_top_left):
    y_offsets = (0, 1, 2, 3, 16, 17, 18, 19)
    for offset in y_offsets:
        draw_line(turtle_object, x_top_left, y_top_left - offset, 0)


def draw_top_bottom(turtle_object, x_top_left, y_top_left):
    x_offsets = (0, 1, 2, 3, 16, 17, 18, 19)
    for offset in x_offsets:
        draw_line(turtle_object, x_top_left + offset, y_top_left, 270)


def draw_left_top(turtle_object, x_top_left, y_top_left):
    draw_square(turtle_object, x_top_left, y_top_left)
    draw_curve(turtle_object, x_top_left, y_top_left - 19, 0)


def draw_left_bottom(turtle_object, x_top_left, y_top_left):
    draw_square(turtle_object, x_top_left, y_top_left - 16)
    draw_curve(turtle_object, x_top_left + 19, y_top_left - 19, 90)


def draw_top_right(turtle_object, x_top_left, y_top_left):
    draw_square(turtle_object, x_top_left + 16, y_top_left)
    draw_curve(turtle_object, x_top_left, y_top_left, 270)


def draw_bottom_right(turtle_object, x_top_left, y_top_left):
    draw_square(turtle_object, x_top_left + 16, y_top_left - 16)
    draw_curve(turtle_object, x_top_left + 19, y_top_left, 180)


def draw_top(turtle_object, x_top_left, y_top_left):
    draw_end(turtle_object, x_top_left, y_top_left, 270)


def draw_bottom(turtle_object, x_top_left, y_top_left):
    draw_end(turtle_object, x_top_left + 19, y_top_left - 19, 90)


def draw_left(turtle_object, x_top_left, y_top_left):
    draw_end(turtle_object, x_top_left, y_top_left - 19, 0)


def draw_right(turtle_object, x_top_left, y_top_left):
    draw_end(turtle_object, x_top_left + 19, y_top_left, 180)


def draw_path_square(turtle_object, x_index, y_index, square_type):
    x_top_left = (x_index - 25) * 20
    y_top_left = (y_index - 12) * -20

    turtle_object.color("red")

    if square_type in ("left->right", "right->left"):
        draw_left_right(turtle_object, x_top_left, y_top_left)

    elif square_type in ("left->top", "top->left"):
        draw_left_top(turtle_object, x_top_left, y_top_left)

    elif square_type in ("left->bottom", "bottom->left"):
        draw_left_bottom(turtle_object, x_top_left, y_top_left)

    elif square_type in ("top->right", "right->top"):
        draw_top_right(turtle_object, x_top_left, y_top_left)

    elif square_type in ("top->bottom", "bottom->top"):
        draw_top_bottom(turtle_object, x_top_left, y_top_left)

    elif square_type in ("bottom->right", "right->bottom"):
        draw_bottom_right(turtle_object, x_top_left, y_top_left)

    elif square_type in ("top->none", "none->top"):
        draw_top(turtle_object, x_top_left, y_top_left)

    elif square_type in ("bottom->none", "none->bottom"):
        print(x_top_left, y_top_left)
        draw_bottom(turtle_object, x_top_left, y_top_left)

    elif square_type in ("left->none", "none->left"):
        draw_left(turtle_object, x_top_left, y_top_left)

    elif square_type in ("right->none", "none->right"):
        draw_right(turtle_object, x_top_left, y_top_left)


def draw_path(turtle_object, path):
    enter_side = "none"
    exit_side = "none"

    for link_index in range(0, len(path)):
        if link_index != 0:
            if path[link_index - 1][0] + 1 == path[link_index][0]:
                enter_side = "left"
            elif path[link_index - 1][0] - 1 == path[link_index][0]:
                enter_side = "right"
            elif path[link_index - 1][1] + 1 == path[link_index][1]:
                enter_side = "top"
            elif path[link_index - 1][1] - 1 == path[link_index][1]:
                enter_side = "bottom"
        else:
            enter_side = "none"

        if link_index != len(path) - 1:
            if path[link_index][0] + 1 == path[link_index + 1][0]:
                exit_side = "right"
            elif path[link_index][0] - 1 == path[link_index + 1][0]:
                exit_side = "left"
            elif path[link_index][1] - 1 == path[link_index + 1][1]:
                exit_side = "top"
            elif path[link_index][1] + 1 == path[link_index + 1][1]:
                exit_side = "bottom"
        else:
            exit_side = "none"

        print(enter_side + "->" + exit_side)

        draw_path_square(turtle_object, path[link_index][0], path[link_index][1], enter_side + "->" + exit_side)
