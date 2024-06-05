import sys
import math

def read_circle_data(filename):
    with open(filename, 'r') as file:
        center_x, center_y = map(float, file.readline().split())
        radius = float(file.readline().strip())
    return center_x, center_y, radius

def read_points(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points

def determine_position(center_x, center_y, radius, point):
    x, y = point
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    circle_data_file = sys.argv[1]
    points_file = sys.argv[2]

    center_x, center_y, radius = read_circle_data(circle_data_file)
    points = read_points(points_file)

    results = [determine_position(center_x, center_y, radius, point) for point in points]

    for result in results:
        print(result)
