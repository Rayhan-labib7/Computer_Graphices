from matplotlib import pyplot as plt

def round(a):
    a1 = int(a)
    a2 = a1+1
    if a-a1>=a2-a:
        return a2
    return a1

def direct_line(x1,y1,x2,y2):
    m = abs(y1-y2)/abs(x1-x2)
    result = []
    if m<0:
        print("Sorry vai")
        return
    b = y1-m*x1
    x_coorinates = []
    y_coorinates = []
    while x1<=x2 or y1<=y2:
        x_coorinates.append(round(x1))
        y_coorinates.append(round(y1))
        result.append((round(x1), round(y1)))
        if m<=1:
            x1 +=1
            y1 = m*x1+b
        else:
            y1+=1
            x1 = (y1-b)/m

    for point in result:
        print(point[0], point[1])
    plt.plot(x_coorinates, y_coorinates, marker="o", markersize=6, markerfacecolor="red")
    plt.show()

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

direct_line(x1, y1, x2, y2)

