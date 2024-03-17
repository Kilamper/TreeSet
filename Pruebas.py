import unittest
from Tree import *
from TreeSet import *


class MyTestCase(unittest.TestCase):
    def test_isEmpty(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        self.assertTrue(ts1.is_empty())

    def test_isNotEmpty(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add(12)
        self.assertFalse(ts1.is_empty())

    def test_containsTrue(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add(1)
        self.assertTrue(ts1.contains(1))

    def test_containsFalse(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add(1)
        self.assertFalse(ts1.contains(2))

    def test_size(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add(8)
        self.assertEqual(ts1.size(), 1)

    def test_insercionFallida(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        self.assertFalse(ts1.add_all([1, "2", 3, 6]))

    def test_delete(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add(8)
        ts1.remove(8)
        self.assertEqual(ts1.size(), 0)

    def test_delete2(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([8, 9])
        ts1.remove(9)
        self.assertEqual(ts1.size(), 1)

    def test_delete3(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([10, 14, 12])
        ts1.remove(14)
        self.assertEqual(ts1.size(), 2)

    def test_delete4(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([1, 9, 2])
        ts1.remove(9)
        self.assertEqual(ts1.size(), 2)

    def test_delete5(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([5, 3, 6, 4, 7, 2])
        ts1.remove(9)
        self.assertEqual(ts1.size(), 6)

    def test_delete6(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([5, 3, 6, 4, 7, 2])
        ts1.remove(3)
        self.assertEqual(ts1.size(), 5)

    def test_clean(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([5, 3, 6])
        ts1.clear()
        self.assertEqual(ts1.size(), 0)

    def test_clone(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        self.assertNotEqual(ts1.clone(), ts1)

    def test_recoloracionRaiz(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add(8)
        self.assertEqual(prototipo.head.color, 1)

    def test_first(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
        self.assertEqual(ts1.first().data, 0)

    def test_last(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
        self.assertEqual(ts1.last().data, 10)

    def test_ceiling(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
        self.assertEqual(ts1.ceiling(9.8), 10)

    def test_ceilingNone(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
        self.assertIsNone(ts1.ceiling(12))

    def test_higher(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([200, 100, 300, 350, 130, 250])
        self.assertEqual(ts1.higher(300), 350)

    def test_higherNone(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([200, 100, 300, 350, 130, 250])
        self.assertIsNone(ts1.higher(400))

    def test_floor(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([200, 100, 300, 350, 130, 250])
        self.assertEqual(ts1.floor(298).data, 250)

    def test_floorEqual(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([200, 100, 300, 350, 130, 250])
        self.assertEqual(ts1.floor(250).data, 250)

    def test_floorNone(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([200, 100, 300, 350, 130, 250])
        self.assertIsNone(ts1.floor(50))

    def test_pollFirst(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([200, 100, 300, 350, 130, 250])
        self.assertEqual(ts1.first().data, ts1.poll_first())

    def test_pollFirstNone(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        self.assertIsNone(ts1.first())

    def test_pollLast(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        ts1.add_all([200, 100, 300, 350, 130, 250])
        self.assertEqual(ts1.poll_last(), ts1.last().data)

    def test_pollLastNone(self):
        prototipo = Tree(None, 0, None)
        ts1 = TreeSet(prototipo)
        self.assertIsNone(ts1.last())
