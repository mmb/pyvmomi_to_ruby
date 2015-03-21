import unittest

from pyvmomi_to_ruby.formatter import format_list
from pyvmomi_to_ruby.or_list import OrList

class TestFormatList(unittest.TestCase):

    def test_mixed(self):
        self.assertEqual(format_list([
            None,
            OrList(['a', 'b']),
            ['a', 'b'],
            ('a', 'b'),
            100,
            'x',
            ]),
            '[nil, {:a => true, :b => true}, ["a", "b"], ["a", "b"], 100, "x"]')

    def test_nested(self):
        self.assertEqual(format_list([[[OrList(['a', 'b'])]]]),
            '[[[{:a => true, :b => true}]]]')
