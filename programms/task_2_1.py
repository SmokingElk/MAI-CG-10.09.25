from __future__ import annotations
from PIL import Image
from math import pi, tan
from typing import Tuple


class Vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Vec3) -> Vec3:
        return Vec3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
    
    def __sub__(self, other: Vec3) -> Vec3:
        return Vec3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
    
    def __mul__(self, number: float) -> Vec3:
        return Vec3(
            self.x * number,
            self.y * number,
            self.z * number
        ) 
    
    def __matmul__(self, other: Vec3) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def mag(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    

WIDTH = 1920
HEIGHT = 1080

FIELD_OF_VIEW = pi / 3

SPHERE_CENTER = Vec3(0, 0, 2100)
RADIUS = 300

SPHERE_COLOR = (255, 0, 0)
BACK_COLOR = (0, 128, 255)

OUT_NAME = "task_2_1_out.png"


def sphere_normal(origin: Vec3, point: Vec3) -> Vec3:
    n = point - origin
    return n * (1 / n.mag())


def scene(ro: Vec3, rd: Vec3) -> Tuple[int, int, int]:
    origin = ro - SPHERE_CENTER

    a = rd @ rd
    b = 2 * (rd @ origin)
    c = origin @ origin - RADIUS**2

    D = b**2 - 4 * a * c

    if D < 0:
        return BACK_COLOR
    
    return SPHERE_COLOR


def f(x: int, y: int) -> Tuple[int, int, int]:
    ro = Vec3(0, 0, 0)
    
    rd = Vec3(
        float(x - WIDTH / 2),
        float(HEIGHT / 2 - y),
        float(WIDTH / 2) / tan(FIELD_OF_VIEW / 2)
    )

    color = scene(ro, rd)

    return color


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