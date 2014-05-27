# -*- coding: utf-8 -*-
# Convert float decimal number to Thai text number
# Copyright (C) 2014, Morange Solution Co.,LTD.
# This file is distributed under the same license as the bahttext package.
# All rights reserved.
# Seksan Poltree <seksan@morange.co.th>, 2014.

import unittest
from bahttext import bahttext


class TestBahtText(unittest.TestCase):

    def test_input_is_a_number_then_can_convert_to_string(self):
        self.assertIsInstance(bahttext(1.0), unicode)

    def test_input_is_not_number_then_raise_error(self):
        with self.assertRaises(TypeError) as ex:
            bahttext('text input')
        self.assertIsInstance(ex.exception, TypeError)

    def test_input_integer_one_digit_can_convert(self):
        self.assertEqual(bahttext(0.0), u'ศูนย์บาทถ้วน')
        self.assertEqual(bahttext(1.0), u'หนึ่งบาทถ้วน')
        self.assertEqual(bahttext(2.0), u'สองบาทถ้วน')
        self.assertEqual(bahttext(5.0), u'ห้าบาทถ้วน')

    def test_number_in_multiple_could_show_sip(self):
        self.assertEqual(bahttext(10.0), u'สิบบาทถ้วน')
        self.assertEqual(bahttext(20.0), u'ยี่สิบบาทถ้วน')
        self.assertEqual(bahttext(50.0), u'ห้าสิบบาทถ้วน')
        self.assertEqual(bahttext(11.0), u'สิบเอ็ดบาทถ้วน')
        self.assertEqual(bahttext(15.0), u'สิบห้าบาทถ้วน')

    def test_input_one_interger_wth_decimal_can_convert(self):
        self.assertEqual(bahttext(1.10), u'หนึ่งบาทสิบสตางค์')
        self.assertEqual(bahttext(2.50), u'สองบาทห้าสิบสตางค์')
        self.assertEqual(bahttext(3.75), u'สามบาทเจ็ดสิบห้าสตางค์')

    def test_number_ending_with_one_could_show_edd(self):
        self.assertEqual(bahttext(4.81), u'สี่บาทแปดสิบเอ็ดสตางค์')

    def test_number_start_with_two_could_show_yee(self):
        self.assertEqual(bahttext(2.21), u'สองบาทยี่สิบเอ็ดสตางค์')

    def test_number_hundred_should_show_roi(self):
        self.assertEqual(bahttext(100.0), u'หนึ่งร้อยบาทถ้วน')
        self.assertEqual(bahttext(101.0), u'หนึ่งร้อยเอ็ดบาทถ้วน')
        self.assertEqual(bahttext(200.0), u'สองร้อยบาทถ้วน')
        self.assertEqual(bahttext(201.0), u'สองร้อยเอ็ดบาทถ้วน')

    def test_number_thoundsand_should_show_pan(self):
        self.assertEqual(bahttext(1000.0), u'หนึ่งพันบาทถ้วน')
        self.assertEqual(bahttext(2000.10), u'สองพันบาทสิบสตางค์')
        self.assertEqual(
            bahttext(3211.51), u'สามพันสองร้อยสิบเอ็ดบาทห้าสิบเอ็ดสตางค์')
        self.assertEqual(bahttext(8000.31), u'แปดพันบาทสามสิบเอ็ดสตางค์')

    def test_number_ten_thoundsand_should_show_muern(self):
        self.assertEqual(bahttext(30000.0), u'สามหมื่นบาทถ้วน')
        self.assertEqual(
            bahttext(98765.10), u'เก้าหมื่นแปดพันเจ็ดร้อยหกสิบห้าบาทสิบสตางค์')
        self.assertEqual(
            bahttext(30211.21), u'สามหมื่นสองร้อยสิบเอ็ดบาทยี่สิบเอ็ดสตางค์')

    def test_number_hundred_thoundsand_should_show_saan(self):
        self.assertEqual(bahttext(800000.0), u'แปดแสนบาทถ้วน')
        self.assertEqual(
            bahttext(258065.81), u'สองแสนห้าหมื่นแปดพันหกสิบห้าบาทแปดสิบเอ็ดสตางค์')

    def test_number_million_should_show_laan(self):
        self.assertEqual(bahttext(3500000.0), u'สามล้านห้าแสนบาทถ้วน')

    def test_number_multiple_million_should_show_multiple_laan(self):
        self.assertEqual(bahttext(12000000.0), u'สิบสองล้านบาทถ้วน')
        self.assertEqual(bahttext(21000000.0), u'ยี่สิบเอ็ดล้านบาทถ้วน')
        self.assertEqual(
            bahttext(51000000000000.51), u'ห้าสิบเอ็ดล้านล้านบาทห้าสิบเอ็ดสตางค์')
        self.assertEqual(
            bahttext(10000000680000.51), u'สิบล้านล้านหกแสนแปดหมื่นบาทห้าสิบเอ็ดสตางค์')

if __name__ == '__main__':
    unittest.main()
