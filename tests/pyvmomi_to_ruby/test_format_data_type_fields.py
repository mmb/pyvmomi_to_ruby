import unittest

from pyvmomi_to_ruby.formatter import format_data_type_fields

class TestFormatDataTypeFields(unittest.TestCase):

    def test_none(self):
        self.assertEqual(format_data_type_fields(None), None)

    def test_zero_flags(self):
        self.assertEqual(format_data_type_fields(
            [('a', 0), ('b', )]),
            [['a'], ['b']])

    def test_no_zero_flags(self):
        self.assertEqual(format_data_type_fields(
            [('a', 1), ('b', 2)]),
            [['a', 1], ['b', 2]])
