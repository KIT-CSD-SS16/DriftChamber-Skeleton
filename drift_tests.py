#! /usr/bin/env python3.4

import unittest


def main():
    all_test = unittest.defaultTestLoader.discover("")
    unittest.TextTestRunner(verbosity=2).run(all_test)


if __name__ == "__main__":
    main()

