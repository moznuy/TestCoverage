import unittest
import django
import os
import sys


sys.path.append(os.path.join(sys.path[0], 'whynot'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whynot.settings')

django.setup()

from FyTest.models import Machine
from FyTest import views


class TestMethods(unittest.TestCase):

    def test_add(self):
        obj = Machine()
        self.assertEqual(obj.state, "idle")

    def test_str(self):
        obj = Machine()
        self.assertEqual(str(obj), 'Car "idle" state')
        obj.key_put()
        self.assertEqual(str(obj), 'Car "engine_starting" state')
        obj.key_turn()
        self.assertEqual(str(obj), 'Car "stopped" state')
        obj.pedal_gas()
        self.assertEqual(str(obj), 'Car "moving" state')
        obj.pedal_stop()
        self.assertEqual(str(obj), 'Car "stopped" state')
        obj.key_out()
        self.assertEqual(str(obj), 'Car "idle" state')


if __name__ == '__main__':
    unittest.main()
