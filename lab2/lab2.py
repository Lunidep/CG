''''
Popov Ilya
M80-306Б-20

16 – гранная прямая правильная пирамида

Тема: Каркасная визуализация выпуклого многогранника. Удаление невидимых линий.
Задание: Разработать формат представления многогранника и процедуру его каркасной отрисовки в ортографической и
изометрической проекциях. Обеспечить удаление невидимых линий и возможность пространственных поворотов и
масштабирования многогранника. Обеспечить автоматическое центрирование и изменение размеров изображения при
изменении размеров окна. 
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.text import Text
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Button

fig = plt.figure()
fig.subplots_adjust(bottom=0.3)
ax = fig.add_subplot(111, projection='3d')
ax.set_title(r"16 – гранная прямая правильная пирамида")

N = 15  # количество граней
segm = np.pi * 2 / N
rotation = 0
radius = 1
#  вершины пирамиды
v = np.array([(np.sin(segm * i + rotation) * radius, np.cos(segm * i + rotation) * radius, 0)
              for i in range(N)])

top = np.array([0, 0, 0.7])
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
ax.set_zlim(0, 1)

#  грани пирамиды
sides = []
for i in range(1, N):
    sides.append([v[i - 1], v[i], top])
sides.append([v[-1], v[0], top])

# основание пирамиды
sides.append(v)

ax.add_collection3d(Poly3DCollection(sides, facecolors='blue', linewidths=1, edgecolors='black', alpha=0.5))


#-------------------------

def remove_func(event):
    ax.add_collection3d(Poly3DCollection(sides, facecolors='blue', linewidths=1, edgecolors='black', alpha=1))
    plt.draw()

remove_button_ax = fig.add_axes([0.4, 0.15, 0.5, 0.05])
remove_button = Button(remove_button_ax, "Удалить невидимые линии")
remove_button.on_clicked(remove_func)


def show_func(event):
    ax.add_collection3d(Poly3DCollection(sides, facecolors='blue', linewidths=1, edgecolors='black', alpha=0.5))
    plt.draw()

show_button_ax = fig.add_axes([0.4, 0.25, 0.5, 0.05])
show_button = Button(show_button_ax, "Показать невидимые линии")
show_button.on_clicked(show_func)

#-------------------------

fig.text(0.1, 0.34, "Проекции:")
def isometric_func(event):
    ax.view_init(elev=30)
    plt.draw()

isometric_button_ax = fig.add_axes([0.1, 0.28, 0.23, 0.05])
isometric_button = Button(isometric_button_ax, "Изометрия")
isometric_button.on_clicked(isometric_func)


def top_func(event):
    ax.view_init(elev=90)
    plt.draw()

top_button_ax = fig.add_axes([0.1, 0.16, 0.23, 0.05])
top_button = Button(top_button_ax, "Вид сверху")
top_button.on_clicked(top_func)


def front_func(event):
    ax.view_init(elev=0)
    plt.draw()

front_button_ax = fig.add_axes([0.1, 0.22, 0.23, 0.05])
front_button = Button(front_button_ax, "Вид спереди")
front_button.on_clicked(front_func)


def bottom_func(event):
    ax.view_init(elev=-90)
    plt.draw()

bottom_button_ax = fig.add_axes([0.1, 0.1, 0.23, 0.05])
bottom_button = Button(bottom_button_ax, "Вид снизу")
bottom_button.on_clicked(bottom_func)

ax.grid()
ax.axis()
plt.show()