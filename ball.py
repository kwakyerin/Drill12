from pico2d import get_canvas_width, load_image


class Ball:
    SPEED = 10

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.image = load_image('ball41x41.png')
        self.is_finished = False

    def update(self):
        self.x += self.direction * self.SPEED
        if self.x < 0 or self.x > get_canvas_width():
            self.is_finished = True

    def draw(self):
        self.image.draw(self.x, self.y)