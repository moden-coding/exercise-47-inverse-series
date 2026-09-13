#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np

from src.inverse_series import inverse_series, main


class InverseSeries(unittest.TestCase):

    def test_first(self):
        L = [1, 2, 3, 1]
        ind = list("abcd")
        s = pd.Series(L, index=ind)
        t = inverse_series(s)
        np.testing.assert_array_equal(t.values, ind, err_msg="Values were incorrect!")
        np.testing.assert_array_equal(t.index, L, err_msg="Index was incorrect!")

    def test_second(self):
        L = list("efgh")
        ind = list("abcd")
        s = pd.Series(L, index=ind)
        t = inverse_series(s)
        np.testing.assert_array_equal(t.values, ind, err_msg="Values were incorrect!")
        np.testing.assert_array_equal(t.index, L, err_msg="Index was incorrect!")

    def test_empty(self):
        s = pd.Series(dtype=object)
        t = inverse_series(s)
        self.assertEqual(len(t), 0, msg="Inversed empty Series should have length zero!")

    def test_called(self):
        with patch("src.inverse_series.inverse_series", wraps=inverse_series) as pis:
            main()
            pis.assert_called()


if __name__ == '__main__':
    unittest.main()
