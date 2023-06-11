def dda(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx

    if m < 0:
        print("Sorry slope is negative.")
        return

    step = max(abs(dx), abs(dy))
    x_inc = dx / float(step)
    y_inc = dy / float(step)
    result = []
    x_coorinates = []
    y_coorinates = []
    print("dx =", dx, ", dy =", dy, ", step =", step)
    print("x_increment =", x_inc, ", y_increment =", y_inc)

    x, y = float(x1), float(y1)

    while x <= x2:
        if x <= x2 and y <= y2:
            result.append((round(x), round(y)))
            x_coorinates.append((round(x)))
            y_coorinates.append((round(y)))
        else:
            break

        x += x_inc
        y += y_inc

    print("----------points-------------")
    for point in result:
        print(point[0], point[1])


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dda(x1, y1, x2, y2)
