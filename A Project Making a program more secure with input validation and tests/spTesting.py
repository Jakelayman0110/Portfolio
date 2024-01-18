import unittest

import spFinalProject as fp


class projectTest(unittest.TestCase):
    # tests checkPass() function
    def testCheckPass(self):
        pass1 = "test"
        pass2 = "testing123"
        pass3 = "ThisIsAPassword"
        pass4 = "123456"
        pass5 = "testing^#^^"

        self.assertEqual(fp.checkPass(pass1), 3)
        self.assertEqual(fp.checkPass(pass2), 0)
        self.assertEqual(fp.checkPass(pass3), 2)
        self.assertEqual(fp.checkPass(pass4), 3)
        self.assertEqual(fp.checkPass(pass5), 1)

    def testGenPass(self):
        # this is gonna be a funky way of testing this
        # not testing anything shorter than 10
        password = fp.genPass(15)
        self.assertEqual(fp.checkPass(password), 0)
        pass


if __name__ == "__main__":
    unittest.main()
