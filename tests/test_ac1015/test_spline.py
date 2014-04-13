#!/usr/bin/env python
#coding:utf-8
# Author:  mozman -- <mozman@gmx.at>
# Purpose: test spline entity
# Created: 12.04.2014
# Copyright (C) 2014, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals

import unittest

import ezdxf


class TestSpline(unittest.TestCase):
    def setUp(self):
        self.dwg = ezdxf.new('AC1015')
        self.layout = self.dwg.modelspace()

    def test_default_settings(self):
        spline = self.layout.add_spline()
        self.assertEqual('0', spline.dxf.layer)
        self.assertEqual(256, spline.dxf.color)
        self.assertEqual('BYLAYER', spline.dxf.linetype)
        self.assertEqual(1.0, spline.dxf.ltscale)
        self.assertEqual(0, spline.dxf.invisible)
        self.assertEqual((0.0, 0.0, 1.0), spline.dxf.extrusion)

        self.assertEqual(0, len(spline.get_knot_values()))
        self.assertEqual(0, len(spline.get_weights()))
        self.assertEqual(0, len(spline.get_control_points()))
        self.assertEqual(0, len(spline.get_fit_points()))

    def test_start_tangent(self):
        spline = self.layout.add_spline()
        spline.dxf.start_tangent = (1, 2, 3)
        self.assertEqual((1, 2, 3), spline.dxf.start_tangent)

    def test_end_tangent(self):
        spline = self.layout.add_spline()
        spline.dxf.end_tangent = (4, 5, 6)
        self.assertEqual((4, 5, 6), spline.dxf.end_tangent)

    def test_knot_values(self):
        spline = self.layout.add_spline()
        values = [1, 2, 3, 4, 5, 6, 7]
        spline.set_knot_values(values)
        self.assertEqual(7, spline.dxf.n_knots)
        self.assertEqual(values, spline.get_knot_values())

    def test_knots_ctx_manager(self):
        spline = self.layout.add_spline()
        values = [1, 2, 3, 4, 5, 6, 7]
        spline.set_knot_values(values)
        with spline.knot_values() as kv:
            kv.extend([8, 9])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], spline.get_knot_values())

    def test_weights(self):
        spline = self.layout.add_spline()
        weights = [1, 2, 3, 4, 5, 6, 7]
        spline.set_weights(weights)
        self.assertEqual(weights, spline.get_weights())

    def test_weights_ctx_manager(self):
        spline = self.layout.add_spline()
        values = [1, 2, 3, 4, 5, 6, 7]
        spline.set_weights(values)
        with spline.weights() as weights:
            weights.extend([8, 9])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], spline.get_weights())

    def test_control_points(self):
        spline = self.layout.add_spline()
        points = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        spline.set_control_points(points)
        self.assertEqual(3, spline.dxf.n_control_points)
        self.assertEqual(points, spline.get_control_points())

    def test_fit_points(self):
        spline = self.layout.add_spline()
        points = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        spline.set_fit_points(points)
        self.assertEqual(3, spline.dxf.n_fit_points)
        self.assertEqual(points, spline.get_fit_points())