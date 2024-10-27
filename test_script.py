import unittest
import numpy as np
from poisson_visualization import (
    main,
    plot_poisson_ascii,
    poisson_distribution,
    validate_lambda_value,
    generate_poisson_distribution,
    LambdaValidationError,
)

ERROR_MSG_INVALID_LAMBDA = (
    "Error: The lambda value must be a numeric value between 1 and 50."
)


class TestPoissonDistribution(unittest.TestCase):
    def test_validate_lambda_value_valid_cases(self):
        valid_cases = [
            ("1", 1.0),
            ("1.0", 1.0),
            ("50", 50.0),
            ("25.5", 25.5),
            ("   10   ", 10.0),
        ]
        for input_value, expected in valid_cases:
            lambda_value = validate_lambda_value([input_value])
            self.assertEqual(lambda_value, expected)

    def test_validate_lambda_value_invalid_cases(self):
        invalid_cases = [
            "1e10",
            "-1000",
            "-5",
            "0",
            "0.1",
            "51",
            "abc",
            "10abc",
            [],
            None,
            "",
            " ",
        ]
        for input_value in invalid_cases:
            with self.assertRaises(LambdaValidationError) as context:
                validate_lambda_value([input_value])
            self.assertEqual(
                str(context.exception),
                "Error: The lambda value must be a numeric value between 1 and 50.",
            )

    # Use assertAlmostEqual to handle floating-point precision errors in calculations.
    def test_generate_poisson_distribution(self):
        lambda_value = 2
        x, y = generate_poisson_distribution(lambda_value)
        self.assertEqual(len(x), 80)
        self.assertEqual(len(y), 80)
        self.assertAlmostEqual(y[0], poisson_distribution(lambda_value, 0), places=4)
        self.assertAlmostEqual(y[1], poisson_distribution(lambda_value, 1), places=4)
        self.assertAlmostEqual(y[2], poisson_distribution(lambda_value, 2), places=4)

    def test_poisson_distribution(self):
        self.assertAlmostEqual(poisson_distribution(2, 0), 0.1353, places=4)
        self.assertAlmostEqual(poisson_distribution(2, 1), 0.2707, places=4)
        self.assertAlmostEqual(poisson_distribution(2, 2), 0.2707, places=4)
        self.assertAlmostEqual(poisson_distribution(2, 3), 0.1804, places=4)

    def test_plot_poisson_ascii(self):
        def run_plot_poisson_test(lambda_value, expected_output):
            x = np.arange(0, 80)
            y = [poisson_distribution(lambda_value, i) for i in x]
            output_list = []
            plot_poisson_ascii(x, y, lambda_value, output_list)
            self.assertEqual(output_list, expected_output)

        expected_output_2 = [
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
        ]
        run_plot_poisson_test(2, expected_output_2)

        expected_output_20_1 = [
            "\nPoisson Distribution (lambda = 20.1):\n",
            "x= 6 | 0.0002 \n",
            "x= 7 | 0.0005 \n",
            "x= 8 | 0.0012 \n",
            "x= 9 | 0.0028 \n",
            "x=10 | 0.0055 \n",
            "x=11 | 0.0101 *\n",
            "x=12 | 0.0169 *\n",
            "x=13 | 0.0262 **\n",
            "x=14 | 0.0376 ***\n",
            "x=15 | 0.0504 *****\n",
            "x=16 | 0.0633 ******\n",
            "x=17 | 0.0748 *******\n",
            "x=18 | 0.0835 ********\n",
            "x=19 | 0.0884 ********\n",
            "x=20 | 0.0888 ********\n",
            "x=21 | 0.0850 ********\n",
            "x=22 | 0.0777 *******\n",
            "x=23 | 0.0679 ******\n",
            "x=24 | 0.0568 *****\n",
            "x=25 | 0.0457 ****\n",
            "x=26 | 0.0353 ***\n",
            "x=27 | 0.0263 **\n",
            "x=28 | 0.0189 *\n",
            "x=29 | 0.0131 *\n",
            "x=30 | 0.0088 \n",
            "x=31 | 0.0057 \n",
            "x=32 | 0.0036 \n",
            "x=33 | 0.0022 \n",
            "x=34 | 0.0013 \n",
            "x=35 | 0.0007 \n",
            "x=36 | 0.0004 \n",
            "x=37 | 0.0002 \n",
            "x=38 | 0.0001 \n",
        ]
        run_plot_poisson_test(20.1, expected_output_20_1)

    def test_main(self):
        test_cases = [
            (["1"], "Poisson Distribution (lambda = 1.0):"),
            (["1.0001"], "Poisson Distribution (lambda = 1.0001):"),
            (["5"], "Poisson Distribution (lambda = 5.0):"),
            (["49.9999"], "Poisson Distribution (lambda = 49.9999):"),
            (["50"], "Poisson Distribution (lambda = 50.0):"),
            (["-5"], ERROR_MSG_INVALID_LAMBDA),
            (["0"], ERROR_MSG_INVALID_LAMBDA),
            (["0.9999"], ERROR_MSG_INVALID_LAMBDA),
            (["50.0001"], ERROR_MSG_INVALID_LAMBDA),
            (["abcde"], ERROR_MSG_INVALID_LAMBDA),
            ([], ERROR_MSG_INVALID_LAMBDA),
            ([None], ERROR_MSG_INVALID_LAMBDA),
            (["1", "2"], ERROR_MSG_INVALID_LAMBDA),
        ]

        for args, expected_message in test_cases:
            result = main(args)
            if expected_message.startswith("Error:"):
                self.assertIn(expected_message, result[0])
                self.assertIn(
                    "Usage: python poisson_visualization.py <lambda>", result[0]
                )
            else:
                self.assertIn(expected_message, result[0])
