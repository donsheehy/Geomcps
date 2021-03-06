import unittest
from trajectories.point import Point

class TestLp(unittest.TestCase):
    def test_2D_point_init(self):
        coords1 = [-7, -4]
        coords2 = [17, 6]
        coords3 = [3, 4]
        coords4 = [0, 0]
        p1 = Point(coords1)
        p2 = Point(coords2)
        p3 = Point(coords3)
        p4 = Point(coords4)

    def test_2D_point_sq_dist(self):
        coords1 = [-7, -4]
        coords2 = [17, 6]
        coords3 = [3, 4]
        coords4 = [0, 0]
        p1 = Point(coords1)
        p2 = Point(coords2)
        p3 = Point(coords3)
        p4 = Point(coords4)
        self.assertEqual(p1.dist_sq(p2), 676.0)
        self.assertEqual(p1.dist_sq(p1), 0.0)
        self.assertEqual(p3.dist_sq(p4), 25.0)

    def test_2D_point_dist(self):
        coords1 = [-7, -4]
        coords2 = [17, 6]
        coords3 = [3, 4]
        coords4 = [0, 0]
        p1 = Point(coords1)
        p2 = Point(coords2)
        p3 = Point(coords3)
        p4 = Point(coords4)
        self.assertEqual(p1.dist(p2), 26.0)
        self.assertEqual(p1.dist(p1), 0.0)
        self.assertEqual(p3.dist(p4), 5.0)

    def test_3D_point_init(self):
        coords1 = [-1, 2, 3]
        coords2 = [4, 0, -3]
        coords3 = [7, 4, 3]
        coords4 = [17, 6, 2]
        p1 = Point(coords1, 0)
        p2 = Point(coords2, 0)
        p3 = Point(coords3, 0)
        p4 = Point(coords4, 0)


    def test_3D_point_sq_dist(self):
        coords1 = [-1, 2, 3]
        coords2 = [4, 0, -3]
        coords3 = [7, 4, 3]
        coords4 = [17, 6, 2]
        p1 = Point(coords1, 0)
        p2 = Point(coords2, 0)
        p3 = Point(coords3, 0)
        p4 = Point(coords4, 0)
        self.assertEqual(p1.dist_sq(p2), 65)
        self.assertEqual(p1.dist_sq(p1), 0.0)
        self.assertEqual(p3.dist_sq(p4), 105)

    def test_3D_point_dist(self):
        coords1 = [-1, 2, 3]
        coords2 = [4, 0, -3]
        coords3 = [7, 4, 3]
        coords4 = [17, 6, 2]
        p1 = Point(coords1, 0)
        p2 = Point(coords2, 0)
        p3 = Point(coords3, 0)
        p4 = Point(coords4, 0)
        self.assertEqual(p1.dist(p2), 65 ** (0.5))
        self.assertEqual(p1.dist(p1), 0.0)
        self.assertEqual(p3.dist(p4), 105**0.5)

    def test_point_eq_degree(self):
        coords1 = [-7, -4]
        coords2 = [17, 6]
        coords3 = [7, 4, 3]
        coords4 = [17, 6, 2]
        p1 = Point(coords1)
        p2 = Point(coords2)
        p3 = Point(coords3, 0)
        p4 = Point(coords4, 0)
        self.assertTrue(p1.eq_degree(p2))
        self.assertTrue(p3.eq_degree(p4))
        self.assertFalse(p1.eq_degree(p3))
        self.assertFalse(p1.eq_degree(p4))
        self.assertFalse(p2.eq_degree(p3))
        self.assertFalse(p2.eq_degree(p4))

if __name__ == '__main__':
    unittest.main()
