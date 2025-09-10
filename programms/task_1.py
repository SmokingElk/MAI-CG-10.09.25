from PIL import Image
from typing import Tuple

WIDTH = 1920
HEIGHT = 1080

OUT_NAME = "task_1_out.png"

CIRCLE_CENTER = (WIDTH / 2, HEIGHT / 2)
RADIUS = 300

CIRCLE_COLOR = (255, 0, 0)
BACK_COLOR = (255, 255, 255)


def f(x: int, y: int) -> Tuple[int, int, int]:
    xTransformed = x - CIRCLE_CENTER[0]
    yTransformed = (HEIGHT - y) - CIRCLE_CENTER[1]

    if xTransformed**2 + yTransformed**2 <= RADIUS**2:
        return CIRCLE_COLOR
    
    return BACK_COLOR


def main():
    image = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = image.load()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = f(x, y)
            pixels[x, y] = color

    image.save(OUT_NAME)


if __name__ == "__main__":
    main()