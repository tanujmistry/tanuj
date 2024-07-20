import turtle
import time

# Set up screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.setworldcoordinates(-500, -500, 500, 500)
screen.title("Connect 4")
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0, 0)

# Constants
ROWS = 6
COLS = 7
STARTX = -450
STARTY = -450 * ROWS / COLS
WIDTH = -2 * STARTX
HEIGHT = -2 * STARTY

# Drawing functions
def draw_rectangle(x, y, w, h, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()

def draw_circle(x, y, r, color):
    turtle.up()
    turtle.goto(x, y - r)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def draw_board():
    draw_rectangle(STARTX, STARTY, WIDTH, HEIGHT, 'light blue')

def draw_pieces():
    row_gap = HEIGHT / ROWS
    col_gap = WIDTH / COLS
    for i in range(ROWS):
        for j in range(COLS):
            x = STARTX + col_gap * (j + 0.5)
            y = STARTY + row_gap * (i + 0.5)
            color = 'white' if board[i][j] == 0 else 'black' if board[i][j] == 1 else 'red'
            draw_circle(x, y, row_gap / 3, color)

def draw():
    draw_board()
    draw_pieces()
    screen.update()

# Game logic
def game_over_lastmove(bb, turn, r, c):
    # Check horizontal
    if sum(1 for i in range(c, COLS) if bb[r][i] == turn) >= 4:
        return turn

    # Check vertical
    if r >= 3 and all(bb[r - i][c] == turn for i in range(1, 4)):
        return turn

    # Check diagonal /
    if sum(1 for i in range(-min(r, c), min(ROWS - r, COLS - c)) if bb[r + i][c + i] == turn) >= 4:
        return turn

    # Check diagonal \
    if sum(1 for i in range(-min(r, COLS - c - 1), min(ROWS - r, c + 1)) if bb[r + i][c - i] == turn) >= 4:
        return turn

    return 0 if all(bb[ROWS - 1][i] != 0 for i in range(COLS)) else -2

def place_piece(bb, turn, col):
    for i in range(ROWS):
        if bb[i][col] == 0:
            bb[i][col] = turn
            return i

def init_board():
    return [[0] * COLS for _ in range(ROWS)]

def place_piece_and_draw(bb, turn, col):
    row = place_piece(bb, turn, col)
    x = STARTX + (WIDTH / COLS) * (col + 0.5)
    y = STARTY + (HEIGHT / ROWS) * (row + 0.5)
    color = 'black' if turn == 1 else 'red'
    for _ in range(5):
        draw_circle(x, y, HEIGHT / ROWS / 3, 'white')
        screen.update()
        time.sleep(0.05)
        draw_circle(x, y, HEIGHT / ROWS / 3, color)
        screen.update()
        time.sleep(0.05)
    return row

def play(x, y):
    global turn, working
    if working:
        return
    working = True
    col_width = WIDTH / COLS
    col = int((x - STARTX) // col_width)
    if 0 <= col < COLS and board[ROWS - 1][col] == 0:
        row = place_piece_and_draw(board, turn, col)
        result = game_over_lastmove(board, turn, row, col)
        if result in [1, -1]:
            screen.textinput('Game over', f'Player {1 if result == 1 else 2} won')
            screen.bye()
        elif result == 0:
            screen.textinput('Game over', 'Tie')
            screen.bye()
        turn = -turn
    working = False

# Main
board = init_board()
draw()
turn = 1
working = False
screen.onclick(play)
screen.mainloop()
