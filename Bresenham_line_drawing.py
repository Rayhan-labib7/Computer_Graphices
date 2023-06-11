import matplotlib.pyplot as plt


def bresenham_line(x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx
    if m >= 1:
        c1 = 2 * dx
        c2 = 2 * (dx - dy)
        p = c1 - dy
    else:
        c1 = 2 * dy
        c2 = 2 * (dy - dx)
        p = c1 - dx

    X = [x1]
    Y = [y1]
    result = []
    result.append((round(x1), round(y1)))
    got = 0
    while got < 2:
        if p < 0:
            p += c1
            if m >= 1:
                y1 += 1
            else:
                x1 += 1
        else:
            p += c2
            y1 += 1;
            x1 += 1

        if got > 0:
            got += 1
        if (x1 == x2 and y1 == y2):
            got = 1
        if x1 - 2 > x2 and y1 - 2 > y2:
            break
        if (x1 <= x2 and y1 <= y2):
            X.append(x1)
            Y.append(y1)
            result.append((round(x1), round(y1)))


    for point in result:
        print(point[0], point[1])
    # Plot the points
    plt.plot(X, Y, marker="o", markersize=6, markerfacecolor="red")
    plt.show()


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

bresenham_line(x1, y1, x2, y2)
