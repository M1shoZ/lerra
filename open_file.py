import numpy as np
import matplotlib.pyplot as plt

# Задаем функцию z = x*y*(2-x-y)
def z_function(x, y):
    return x*y*(2-x-y)

# Создаем сетку значений x и y
x = np.linspace(-1, 3, 100)
y = np.linspace(-1, 3, 100)
X, Y = np.meshgrid(x, y)

# Вычисляем значения функции z на сетке
Z = z_function(X, Y)

# Создаем график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Устанавливаем метки осей
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Отображаем график
plt.show()
