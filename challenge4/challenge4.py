import unittest
from fibonacci import Fibonacci
from num2string import int_to_english

class challenge4(unittest.TestCase):

    def setUp (self):
        print("Getting ready to run Fibonacci.")

    def tearDown(self):
        print("Completed running Fibonacci.")

    def test_challenge4(self):
        # print("go to ...")

        f = Fibonacci()
        fibo = f.fibo

        for i in range(1, 49):
            print("The numerical value of level", i, "of the fibonacci sequence is", int_to_english(fibo(i)))


if __name__ == '__main__':
    unittest.main()