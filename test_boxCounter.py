from unittest import TestCase

from day2 import BoxChecksum

class TestBoxCounter(TestCase):
    def setUp(self):
        self.bc = BoxChecksum()

    def to_input(self, s):
        return s.replace(', ', '\n')


    def test1_1(self):
        input_ = self.to_input("abcdef, bababc, abbcde, abcccd, aabcdd, abcdee, ababab")
        self.assertEquals(12, self.bc.checksum_boxes(input_))

    def test2_1(self):
        input_ = self.to_input("abcde, fghij klmno, pqrst fguij, axcye, wvxyz")
        self.assertEquals("fgij", self.bc.detect_neighbors(input_))
