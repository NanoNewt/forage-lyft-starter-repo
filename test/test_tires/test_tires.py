import unittest
from tires.octoprime_tires import OctoprimeTires
from tires.carrigan_tires import CarriganTires

class TestOctoprimeTires(unittest.TestCase):
    def test_should_be_serviced(self):
        tires = OctoprimeTires([0.8, 0.8, 0.8, 0.7])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = OctoprimeTires([0.1, 0.2, 0.4, 0.2])
        self.assertFalse(tires.needs_service())

class TestCarriganTires(unittest.TestCase):
    def test_should_be_serviced(self):
        tires = CarriganTires([0.1, 0.3, 0.2, 0.9])
        self.assertTrue(tires.needs_service())
        
    def test_should_not_be_serviced(self):
        tires = CarriganTires([0.1, 0.2, 0.4, 0.2])
        self.assertFalse(tires.needs_service())