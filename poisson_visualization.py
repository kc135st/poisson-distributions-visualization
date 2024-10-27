import math
import numpy as np

MIN_PROBABILITY_DISPLAY_LIMIT = 0.0001
ERROR_MSG_INVALID_LAMBDA = "Error: The lambda value must be a numeric value between 1 and 50."


class LambdaValidationError(ValueError):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


def poisson_distribution(lambda_value, k):
    return (lambda_value**k) * math.exp(-lambda_value) / math.factorial(k)


def plot_poisson_ascii(x, y, lambda_value, output_list):
    output_list.append(f"\nPoisson Distribution (lambda = {lambda_value}):\n")
    previous_prob = None

    for i, prob in enumerate(y):
        # Skip probabilities below the minimum display limit
        if prob < MIN_PROBABILITY_DISPLAY_LIMIT:
            if previous_prob is None or previous_prob >= MIN_PROBABILITY_DISPLAY_LIMIT:
                output_list.append(f"x={x[i]:2d} | 0.0000\n")
        else:
            # Display a star for each 0.01 in the probability
            stars = '*' * int(prob * 100)
            output_list.append(f"x={x[i]:2d} | {prob:.4f} {stars}\n")
        previous_prob = prob


def validate_lambda_value(args):
    if not args or len(args) != 1 or args[0] is None:
        raise LambdaValidationError(ERROR_MSG_INVALID_LAMBDA)

    try:
        lambda_value = float(args[0])
        if not (1 <= lambda_value <= 50):
            raise LambdaValidationError(ERROR_MSG_INVALID_LAMBDA)

        return lambda_value
    except (ValueError, TypeError):
        raise LambdaValidationError(ERROR_MSG_INVALID_LAMBDA)


def generate_poisson_distribution(lambda_value):
    # For λ values 1 to 50, the Poisson probabilities are well-represented up to x = 80.
    # In this tool, only up to the 4th decimal place is displayed.
    x = np.arange(0, 80)
    y = [poisson_distribution(lambda_value, i) for i in x]
    return x, y


def main(args=None):
    output_list = []

    try:
        lambda_value = validate_lambda_value(args)
    except LambdaValidationError as e:
        output_list.append(
            e.message + "\nUsage: python poisson_visualization.py <lambda>\n")
        return output_list

    x, y = generate_poisson_distribution(lambda_value)
    plot_poisson_ascii(x, y, lambda_value, output_list)

    return output_list


if __name__ == "__main__":
    import sys
    result = main(sys.argv[1:])
    for line in result:
        print(line, end="")
