import matplotlib.pyplot as plt


def bresenham_circle(h, k, r):
    x, y = 0, r
    p = 3 - 2 * r
    step = 1
    X = []
    Y = []
    while (x <= y):
        X.append(x + h)
        Y.append(y + k)
        X.append(y + k)
        Y.append(x + h)
        X.append(-x + h)
        Y.append(y + k)
        X.append(y + k)
        Y.append(-x + h)
        X.append(-x + h)
        Y.append(-y + k)
        X.append(-y + k)
        Y.append(-x + h)
        X.append(x + h)
        Y.append(-y + k)
        X.append(-y + k)
        Y.append(x + h)

        step += 1
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1
        x += 1

    # Plot the points
    plt.scatter(X, Y)
    for i in range(len(X)):
        plt.annotate(f'({X[i]}, {Y[i]})', (X[i], Y[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.show()

h = int(input("Enter h: "))
k = int(input("Enter k: "))
r = int(input("Enter redius: "))

bresenham_circle(h, k, r)
