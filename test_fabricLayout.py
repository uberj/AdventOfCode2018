from unittest import TestCase

from day3 import FabricLayout


class TestFabricLayout(TestCase):
    def setUp(self):
        self.fl = FabricLayout()

    def to_input(self, s):
        return s.replace(', ', '\n')

    def test1_1(self):
        input_ = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        self.assertEquals(4, len(self.fl.overlapping_inches(input_)))

    def test2_1(self):
        input_ = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        self.assertEquals("3", self.fl.disjoint_claim(input_))
