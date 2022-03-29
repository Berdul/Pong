import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 700, 500
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (20, 20, 20)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WINDOW_WIDTH - PADDLE_WIDTH - 10, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                          PADDLE_HEIGHT)
    ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 10)
    while run:
        clock.tick(FPS)

        draw(window, [left_paddle, right_paddle], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        ball.move()

    pygame.quit()


def draw(win, paddles, ball):
    win.fill(BLACK)
    for paddle in paddles:
        paddle.draw(win)
    ball.draw(win)
    pygame.draw.line(win, GREY, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), 4)
    pygame.display.update()


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_z] and left_paddle.y - left_paddle.SPEED > 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.SPEED + PADDLE_HEIGHT < WINDOW_HEIGHT:
        left_paddle.move(up=False)
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.SPEED > 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.SPEED + PADDLE_HEIGHT < WINDOW_HEIGHT:
        right_paddle.move(up=False)


class Paddle:
    COLOR = WHITE
    SPEED = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.SPEED
        else:
            self.y += self.SPEED


class Ball:
    MAX_SPEED = 5;

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_speed = self.MAX_SPEED
        self.y_speed = 0

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

if __name__ == '__main__':
    main()
