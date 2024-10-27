import math
import numpy as np
from typing import List, Optional, Tuple

MIN_PROBABILITY_DISPLAY_LIMIT: float = 0.0001
ERROR_MSG_INVALID_LAMBDA: str = (
    "Error: The lambda value must be a numeric value between 1 and 50."
)


class LambdaValidationError(ValueError):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message: str = message


def poisson_distribution(lambda_value: float, k: int) -> float:
    return (lambda_value**k) * math.exp(-lambda_value) / math.factorial(k)


def plot_poisson_ascii(
    x: np.ndarray[np.int_, np.dtype[np.int_]],
    y: List[float],
    lambda_value: float,
    output_list: List[str],
) -> None:
    output_list.append(f"\nPoisson Distribution (lambda = {lambda_value}):\n")

    for i, prob in enumerate(y):
        if prob >= MIN_PROBABILITY_DISPLAY_LIMIT:
            # Display a star for each 0.01 in the probability
            stars = "*" * int(prob * 100)
            output_list.append(f"x={x[i]:2d} | {prob:.4f} {stars}\n")


def validate_lambda_value(args: Optional[List[Optional[str]]]) -> float:
    if not args or len(args) != 1 or args[0] is None:
        raise LambdaValidationError(ERROR_MSG_INVALID_LAMBDA)

    try:
        lambda_value = float(args[0])
        if not (1 <= lambda_value <= 50):
            raise LambdaValidationError(ERROR_MSG_INVALID_LAMBDA)

        return lambda_value
    except (ValueError, TypeError):
        raise LambdaValidationError(ERROR_MSG_INVALID_LAMBDA)


def generate_poisson_distribution(
    lambda_value: float,
) -> Tuple[np.ndarray[np.int_, np.dtype[np.int_]], List[float]]:
    # For λ values 1 to 50, the Poisson probabilities are well-represented up to x = 80.
    # In this tool, only up to the 4th decimal place is displayed.
    x: np.ndarray[np.int_, np.dtype[np.int_]] = np.arange(0, 80)
    y: List[float] = [poisson_distribution(lambda_value, i) for i in x]
    return x, y


def main(args: Optional[List[Optional[str]]] = None) -> List[str]:
    output_list: List[str] = []

    try:
        lambda_value = validate_lambda_value(args)
    except LambdaValidationError as e:
        output_list.append(
            e.message + "\nUsage: python poisson_visualization.py <lambda>\n"
        )
        return output_list

    x, y = generate_poisson_distribution(lambda_value)
    plot_poisson_ascii(x, y, lambda_value, output_list)

    return output_list


if __name__ == "__main__":
    import sys

    result = main([arg for arg in sys.argv[1:]])
    for line in result:
        print(line, end="")
