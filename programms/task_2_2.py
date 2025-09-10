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
LIGHT_DIR = Vec3(-1, -1, -1)
RADIUS = 300

SPHERE_COLOR = (255, 0, 0)
BACK_COLOR = (0, 128, 255)

OUT_NAME = "task_2_2_out.png"


def sphere_normal(origin: Vec3, point: Vec3) -> Vec3:
    n = point - origin
    return n * (1 / n.mag())


def scene(ro: Vec3, rd: Vec3) -> Tuple[Vec3, Tuple[int, int, int]]:
    origin = ro - SPHERE_CENTER

    a = rd @ rd
    b = 2 * (rd @ origin)
    c = origin @ origin - RADIUS**2

    D = b**2 - 4 * a * c

    if D < 0:
        return [Vec3(0, 0, 0), BACK_COLOR]
    
    t1 = (-b + D**0.5) / (2 * a) 
    t2 = (-b + D**0.5) / (2 * a)

    t = min(t1, t2)

    pos = ro + rd * t
    normal = sphere_normal(SPHERE_CENTER, pos)

    return [normal, SPHERE_COLOR]


def f(x: int, y: int) -> Tuple[int, int, int]:
    ro = Vec3(0, 0, 0)
    
    rd = Vec3(
        float(x - WIDTH / 2),
        float(HEIGHT / 2 - y),
        float(WIDTH / 2) / tan(FIELD_OF_VIEW / 2)
    )

    [normal, color] = scene(ro, rd)

    if normal.mag() < 0.01:
        return BACK_COLOR
    
    l = LIGHT_DIR * (1 / LIGHT_DIR.mag())

    light_level = max(0, normal @ (l * -1))

    shaded = (
        int(color[0] * light_level),
        int(color[1] * light_level),
        int(color[2] * light_level),
    )

    return shaded


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