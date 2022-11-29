'''
Тема: Построение плоских полиномиальных кривых.
Задание: Написать программу, строящую полиномиальную кривую по заданным точкам. Обеспечить возможность
изменения позиции точек.

NURB-кривая. n = 6, k = 3. Узловой вектор неравномерный. Веса точек различны и модифицируются
'''

from geomdl import NURBS
from geomdl import utilities
from geomdl.visualization import VisMPL

curve = NURBS.Curve()

curve.degree = 3
curve.ctrlpts = [[2, 8, 0], [3, 3, 0], [4, 10, 0], [5, 1, 0], [7, 5, 0], [8, 4, 0]]

# вектор узлов
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# гладкость кривой
curve.delta = 0.0001

curve.vis = VisMPL.VisCurve2D()
curve.render()