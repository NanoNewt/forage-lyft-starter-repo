import unittest
from tires.octoprime_tires import OctoprimeTires
from tires.carrigan_tires import CarriganTires

class TestOctoprimeTires(unittest.TestCase):
    def test_should_be_serviced(self):
        tires = OctoprimeTires([1,1,1,1])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = OctoprimeTires([0,0,0,0])
        self.assertFalse(tires.needs_service())

class TestCarriganTires(unittest.TestCase):
    def test_should_be_serviced(self):
        tires = CarriganTires([1,1,1,1])
        self.assertTrue(tires.needs_service())
        
    def test_should_not_be_serviced(self):
        tires = CarriganTires([0,0,0,0])
        self.assertFalse(tires.needs_service())