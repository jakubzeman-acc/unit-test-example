import unittest
from src import main


class GlobalVarTest(unittest.TestCase):

    def test_global_var_change(self):
        self.assertEqual(1, main.global_variable_example)
        main.change_global_var(2)
        self.assertEqual(2, main.global_variable_example)
