import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400  # Milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += 20

    # Add new head to snake body.
    snake.append(new_head)

    # Remove last segment
    snake.pop(0)

    # Draw snake 
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    # Refresh screen
    screen.update()

    # Rinse and repeat
    turtle.ontimer(move_snake, DELAY)

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Create snake as a list of coordiante pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"

# Draw snake for the first time.
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# Set animation in motion
move_snake()


# Finish nicely
screen.mainloop()
