from math import sin, cos, pi


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def func(x):
    return -4 * x * sin(x)


def der(x):
    return -4 * x * cos(x) + -4 * sin(x)


def middle_point(a, b, eps):
    middle = (a + b) / 2
    derivative = der(middle)
    if abs(b - a) < eps:
        return middle
    if derivative > 0:
        return middle_point(a, middle, eps)
    else:
        return middle_point(middle, b, eps)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(middle_point(0, pi, 10 ** -10))
