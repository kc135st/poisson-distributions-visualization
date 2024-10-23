import unittest
import numpy as np

from poisson_visualization import main, plot_poisson_ascii, poisson_distribution


class TestPoissonDistribution(unittest.TestCase):

    ERROR_MSG = "Error: The lambda value must be a numeric value between 1 and 50."

    def assert_poisson_output(self, lambda_value, expected_text):
        result = main([lambda_value])
        self.assertIn(expected_text, result[0])

    def assert_error_message(self, lambda_value):
        result = main([lambda_value])
        self.assertIn(self.ERROR_MSG, result[0])

    def test_valid_lambdas(self):
        self.assert_poisson_output("1", "Poisson Distribution (lambda = 1.0):")
        self.assert_poisson_output(
            "1.", "Poisson Distribution (lambda = 1.0):")
        self.assert_poisson_output(
            "1.0", "Poisson Distribution (lambda = 1.0):")
        self.assert_poisson_output(
            "1.00000", "Poisson Distribution (lambda = 1.0):")
        self.assert_poisson_output(
            "50", "Poisson Distribution (lambda = 50.0):")
        self.assert_poisson_output(
            "   10   ", "Poisson Distribution (lambda = 10.0):")
        self.assert_poisson_output(
            "25.5", "Poisson Distribution (lambda = 25.5):")

    def test_invalid_lambdas(self):
        self.assert_error_message("-1000")
        self.assert_error_message("-5")
        self.assert_error_message("0.0")
        self.assert_error_message("0")
        self.assert_error_message(".1")
        self.assert_error_message("0.1")
        self.assert_error_message("0.9")
        self.assert_error_message("50.1")
        self.assert_error_message("51")
        self.assert_error_message("1000000")
        self.assert_error_message("9999999")
        self.assert_error_message("0.00001")
        self.assert_error_message("1e10")
        self.assert_error_message("abc")
        self.assert_error_message("10abc")
        self.assert_error_message([])
        self.assert_error_message(None)
        self.assert_error_message("")
        self.assert_error_message(" ")

    def test_plot_poisson_ascii(self):
        lambda_value = 2
        x = np.arange(0, 11)
        y = [poisson_distribution(lambda_value, i) for i in x]
        output_list = []
        plot_poisson_ascii(x, y, lambda_value, output_list)

        expected_output = [
            "\nPoisson Distribution (lambda = 2):\n",
            "x= 0 | 0.1353 *************\n",
            "x= 1 | 0.2707 ***************************\n",
            "x= 2 | 0.2707 ***************************\n",
            "x= 3 | 0.1804 ******************\n",
            "x= 4 | 0.0902 *********\n",
            "x= 5 | 0.0361 ***\n",
            "x= 6 | 0.0120 *\n",
            "x= 7 | 0.0034 \n",
            "x= 8 | 0.0009 \n",
            "x= 9 | 0.0002 \n",
            "x=10 | 0.0000\n"
        ]

        self.assertEqual(output_list, expected_output)


if __name__ == '__main__':
    unittest.main()
