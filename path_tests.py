import unittest
from shapely.geometry import Point
from drawer import show_plot
from path import find_shortest_path

class PathTests(unittest.TestCase):
    def test_main_flow(self):
        gates = [
            (Point(5, 3), Point(9.68, 3.82)),       # A, B
            (Point(2.8, 6.4), Point(7.36, 7.44)),   # C, D
            (Point(4.06, 11.84), Point(8.24, 9.7)), # E, F
            (Point(6.82, 14.04), Point(11.36, 12.4)), # G, H
            (Point(4.88, 15.36), Point(14.24, 14.24)), # I, J
            (Point(12.58, 18), Point(17.02, 10.48)), # K, L
            (Point(20.24, 15.74), Point(18.38, 11.64)), # M, N
            (Point(21.58, 13.92), Point(22.22, 7.24)), # O, P 
            (Point(23.84, 15.28), Point(25.7, 10.76)), # Q, R
            (Point(30.1, 11.76), Point(25.82, 8.52)),  # S, T
            (Point(29.282, 6.866), Point(25.938, 6.91)), # U, V
            (Point(31.042, 4.116), Point(28, 4)),       # W, Z
        ]
        start_point, end_point = Point(6, 2), Point(30, 2)
        path = find_shortest_path(gates, start_point, end_point)
        show_plot(gates, path)

    def test_reversed_gate(self):
        gates = [
            (Point(5, 3), Point(9.68, 3.82)),       # A, B
            (Point(2.8, 6.4), Point(7.36, 7.44)),   # C, D
            (Point(4.88, 15.36), Point(14.24, 14.24)), # I, J
            (Point(17.02, 2.48), Point(12.58, 25)), # K, L <-- swapped points, supposed to go to edge
            (Point(20.24, 15.74), Point(18.38, 11.64)), # M, N
            (Point(31.042, 4.116), Point(28, 4)),       # W, Z
        ]
        start_point, end_point = Point(6, 2), Point(30, 2)
        path = find_shortest_path(gates, start_point, end_point)
        show_plot(gates, path)


if __name__ == '__main__':
    unittest.main()
