import math

class GeometryCalculator:

    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":

    calculator = GeometryCalculator()

# TODO: Implement the feature to calculate the area of a rectangle # 
length = 12
width = 7

print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)} sq.units")