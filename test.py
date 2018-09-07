import unittest
from Fibonacci import Fibonacci


class TestFibonacciMethods(unittest.TestCase):

	def test_fibonacci(self):
		fib = Fibonacci(7)
		self.assertEqual(fib.get(), 13)

		
class TestStringMethods(unittest.TestCase):

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])



if __name__ == '__main__':

	suite1 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
	suite2 = unittest.TestLoader().loadTestsFromTestCase(TestFibonacciMethods)
	alltests = unittest.TestSuite([suite1, suite2])
	unittest.TextTestRunner(verbosity=2).run(alltests)


	'''
	Existing methods:

	Method							Checks that	
	assertEqual(a, b)					a == b	 
	assertNotEqual(a, b)				a != b	 
	assertTrue(x)						bool(x) is True	 
	assertFalse(x)						bool(x) is False	 
	assertIs(a, b)						a is b	
	assertIsNot(a, b)					a is not b	
	assertIsNone(x)						x is None	
	assertIsNotNone(x)					x is not None	
	assertIn(a, b)						a in b	
	assertNotIn(a, b)					a not in b	
	assertIsInstance(a, b)				isinstance(a, b)	
	assertNotIsInstance(a, b)			not isinstance(a, b)	
	assertAlmostEqual(a, b)				round(a-b, 7) == 0	 
	assertNotAlmostEqual(a, b)			round(a-b, 7) != 0	 
	assertGreater(a, b)					a > b	
	assertGreaterEqual(a, b)			a >= b	
	assertLess(a, b)					a < b	
	assertLessEqual(a, b)				a <= b	
	assertRegexpMatches(s, r)			r.search(s)	
	assertNotRegexpMatches(s, r)		not r.search(s)	
	assertItemsEqual(a, b)				sorted(a) == sorted(b) and works with unhashable objs	
	assertDictContainsSubset(a, b)		all the key/value pairs in a exist in b	
	assertMultiLineEqual(a, b)			strings	
	assertSequenceEqual(a, b)			sequences	
	assertListEqual(a, b)				lists	
	assertTupleEqual(a, b)				tuples	
	assertSetEqual(a, b)				sets or frozensets	
	assertDictEqual(a, b)				dicts	
	'''