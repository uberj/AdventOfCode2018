from unittest import TestCase

from FrequencyCompensator import FrequencyCompensator


class TestFrequencyCompensator(TestCase):
    def setUp(self):
        self.fc = FrequencyCompensator()

    def to_input(self, s):
        return s.replace(', ', '\n')

    def test1_1(self):
        input_ = self.to_input("+1, +1, +1")
        self.assertEquals(3, self.fc.compensate_from_input(input_))

    def test1_2(self):
        input_ = self.to_input("+1, +1, -2")
        self.assertEquals(0, self.fc.compensate_from_input(input_))

    def test1_3(self):
        input_ = self.to_input("-1, -2, -3")
        self.assertEquals(-6, self.fc.compensate_from_input(input_))

    def test1_3(self):
        input_ = self.to_input("-1, -2, -3")
        self.assertEquals(-6, self.fc.compensate_from_input(input_))

    def test2_1(self):
        input_ = self.to_input("+1, -1")
        self.assertEquals(0, self.fc.detect_cycle(input_))

    def test2_2(self):
        input_ = self.to_input("+3, +3, +4, -2, -4")
        self.assertEquals(10, self.fc.detect_cycle(input_))

    def test2_3(self):
        input_ = self.to_input("-6, +3, +8, +5, -6")
        self.assertEquals(5, self.fc.detect_cycle(input_))

    def test2_4(self):
        input_ = self.to_input("+7, +7, -2, -7, -4")
        self.assertEquals(14, self.fc.detect_cycle(input_))
