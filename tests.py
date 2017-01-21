import unittest

class Test1(unittest.TestCase):
    def testPass(self):
        self.assertLess(1, 2)
    def testFail(self):
        self.assertTrue(2 == 1)
