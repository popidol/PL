with open('circle.txt', 'r') as f:
    h, k = map(float, f.readline().split())
    a, b = map(float, f.readline().split())

with open('dot.txt', 'r') as f:
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