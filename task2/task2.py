import sys

if len(sys.argv) != 3:
    print("Не все аргументы")
    sys.exit(1)

circle_file = sys.argv[1]
dot_file = sys.argv[2]

with open(circle_file, 'r') as f:
    h, k = map(float, f.readline().split())
    a, b = map(float, f.readline().split())
with open(dot_file, 'r') as f:
    for line in f:
        x, y = map(float, line.split())
        dx, dy = x - h, y - k
        value = (dx * dx) / (a * a) + (dy * dy) / (b * b)
        if abs(value - 1) < 1e-6:
            print(0)
        elif value < 1:
            print(1)
        else:
            print(2)