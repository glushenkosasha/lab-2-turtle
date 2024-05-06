import math


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.pivot = None

    def set_pivot(self, pivot_x, pivot_y):
        self.pivot = (pivot_x, pivot_y)

    def rotate(self, angle):
        if self.pivot is None:
            raise ValueError("Pivot point has not been set.")

        angle_rad = math.radians(angle)

        translated_x1 = self.x1 - self.pivot[0]
        translated_y1 = self.y1 - self.pivot[1]
        translated_x2 = self.x2 - self.pivot[0]
        translated_y2 = self.y2 - self.pivot[1]
        translated_x3 = self.x3 - self.pivot[0]
        translated_y3 = self.y3 - self.pivot[1]

        rotated_x1 = translated_x1 * math.cos(angle_rad) - translated_y1 * math.sin(angle_rad)
        rotated_y1 = translated_x1 * math.sin(angle_rad) + translated_y1 * math.cos(angle_rad)
        rotated_x2 = translated_x2 * math.cos(angle_rad) - translated_y2 * math.sin(angle_rad)
        rotated_y2 = translated_x2 * math.sin(angle_rad) + translated_y2 * math.cos(angle_rad)
        rotated_x3 = translated_x3 * math.cos(angle_rad) - translated_y3 * math.sin(angle_rad)
        rotated_y3 = translated_x3 * math.sin(angle_rad) + translated_y3 * math.cos(angle_rad)

        self.x1 = rotated_x1 + self.pivot[0]
        self.y1 = rotated_y1 + self.pivot[1]
        self.x2 = rotated_x2 + self.pivot[0]
        self.y2 = rotated_y2 + self.pivot[1]
        self.x3 = rotated_x3 + self.pivot[0]
        self.y3 = rotated_y3 + self.pivot[1]

    def stretch(self, factor):
        if self.pivot is None:
            raise ValueError("Pivot point has not been set.")

        translated_x1 = self.x1 - self.pivot[0]
        translated_y1 = self.y1 - self.pivot[1]
        translated_x2 = self.x2 - self.pivot[0]
        translated_y2 = self.y2 - self.pivot[1]
        translated_x3 = self.x3 - self.pivot[0]
        translated_y3 = self.y3 - self.pivot[1]

        stretched_x1 = translated_x1 * factor
        stretched_y1 = translated_y1 * factor
        stretched_x2 = translated_x2 * factor
        stretched_y2 = translated_y2 * factor
        stretched_x3 = translated_x3 * factor
        stretched_y3 = translated_y3 * factor

        self.x1 = stretched_x1 + self.pivot[0]
        self.y1 = stretched_y1 + self.pivot[1]
        self.x2 = stretched_x2 + self.pivot[0]
        self.y2 = stretched_y2 + self.pivot[1]
        self.x3 = stretched_x3 + self.pivot[0]
        self.y3 = stretched_y3 + self.pivot[1]


triangle = Triangle(0, 0, 3, 0, 0, 4)

triangle.set_pivot(1, 1)

triangle.rotate(45)

triangle.stretch(2)

print("Triangle vertices after rotation and stretching:")
print("Vertex 1:", (triangle.x1, triangle.y1))
print("Vertex 2:", (triangle.x2, triangle.y2))
print("Vertex 3:", (triangle.x3, triangle.y3))
