from io import BytesIO as StringIO

import unittest

from pyVmomi.VmomiSupport import CreateManagedType

class TestCreateManagedType(unittest.TestCase):

    def setUp(self):
        self.out = StringIO()

    def test_mixed(self):
        CreateManagedType('a', 'b', 'c', 'd', None, [None], self.out)
        self.assertEqual(self.out.getvalue(),
            '    create_managed_type("a", "b", "c", "d", nil, [nil])\n')
