import unittest
import Otplast


# from otp import generate_otp


class TestgenerateOTP(unittest.TestCase):

    def testcase1(self):
        size = 4

        Email = Otplast.emailsender
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        res = Otplast.otp(4)
        self.assertEqual(len(res), size)

    def testcase2(self):
        size = 4

        Email = Otplast.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)



        res = Otplast.otp(4)
        self.assertEqual(len(res), size)

    def testcase3(self):
        size = 4

        Email = Otplast.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

        res = Otplast.otp(4)
        self.assertEqual(len(res), size)

    def testcase4(self):
        size = 4

        Email = Otplast.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

        res = Otplast.otp(4)
        self.assertEqual(len(res), size)


if __name__ == '__main__':

    unittest.main()