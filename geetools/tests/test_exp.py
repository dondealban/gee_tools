# coding=utf-8
import unittest
import ee
from geetools import tools
ee.Initialize()

class TestExp(unittest.TestCase):

    def setUp(self):
        self.l8SR = ee.Image("LANDSAT/LC8_SR/LC82310772014043")
        self.p_l8SR_no_cloud = ee.Geometry.Point([-66.0306, -24.9338])

    def test_expressions(self):
        from geetools import expressions
        generator = expressions.ExpGen()
        exp_max = generator.max("b('B1')", "b('B2')")
        exp_min = generator.min("b('B1')", "b('B2')")

        img_max = self.l8SR.expression(exp_max).select([0], ["max"])
        img_min = self.l8SR.expression(exp_min).select([0], ["min"])

        vals_max = tools.get_value(img_max, self.p_l8SR_no_cloud, 30)
        vals_min = tools.get_value(img_min, self.p_l8SR_no_cloud, 30)

        self.assertEqual(vals_max["max"], 580)
        self.assertEqual(vals_min["min"], 517)