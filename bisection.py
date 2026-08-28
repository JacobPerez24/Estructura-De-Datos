import math

def bisection_method(func, a, b, tolerance=1e-6, max_iterations=100):
    # Asegura que a < b, sin importar el orden en que los ingrese el usuario
    if a > b:
        a, b = b, a

    fa = func(a)
    if fa * func(b) >= 0:
        raise ValueError("The function must change sign on the interval [a, b].")

    for i in range(max_iterations):
        c = (a + b) / 2  # Midpoint
        fc = func(c)

        if abs(fc) < tolerance or (b - a) / 2 < tolerance:
            return c

        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc  # actualizamos fa solo cuando a cambia

    raise RuntimeError("Maximum number of iterations reached without finding a root.")

a = float(input('Input interval (a): '))
b = float(input('Input interval (b): '))
root = bisection_method(lambda x: x**2 + 2*x - 8, a, b)
print(f"The root is approximately: {root}")