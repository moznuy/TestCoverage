import unittest
import django
import os
import sys


sys.path.append(os.path.join(sys.path[0], 'whynot'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whynot.settings')

django.setup()

from FyTest.models import TestMachine


class TestMethods(unittest.TestCase):

    def test_add(self):
        obj = TestMachine()
        self.assertEqual(obj.state, "idle")


if __name__ == '__main__':
    unittest.main()
