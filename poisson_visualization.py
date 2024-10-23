import math
import numpy as np

MIN_PROBABILITY_DISPLAY_LIMIT = 0.0001


def poisson_distribution(lambda_value, k):
    """Calculate Poisson probability for a given lambda and k."""
    return (lambda_value ** k) * math.exp(-lambda_value) / math.factorial(k)


def plot_poisson_ascii(x, y, lambda_value, output_list):
    """Generate Poisson distribution ASCII plot and store it in output_list."""
    output_list.append(f"\nPoisson Distribution (lambda = {lambda_value}):\n")
    previous_prob = None
    for i, prob in enumerate(y):
        if prob < MIN_PROBABILITY_DISPLAY_LIMIT:
            if previous_prob is None or previous_prob >= MIN_PROBABILITY_DISPLAY_LIMIT:
                output_list.append(f"x={x[i]:2d} | 0.0000\n")
        else:
            stars = '*' * int(prob * 100)  # Display one '*' for every 0.01
            output_list.append(f"x={x[i]:2d} | {prob:.4f} {stars}\n")
        previous_prob = prob


def validate_lambda_value(args):
    """Parse and validate the lambda value from the arguments."""
    if not args or len(args) != 1 or args[0] is None:
        return None, "Error: The lambda value must be a numeric value between 1 and 50."

    try:
        lambda_value = float(args[0])
        if not (1 <= lambda_value <= 50):
            return None, "Error: The lambda value must be a numeric value between 1 and 50."
        return lambda_value, None
    except (ValueError, TypeError):
        return None, "Error: The lambda value must be a numeric value between 1 and 50."


def generate_poisson_distribution(lambda_value):
    """Generate x and y values for the Poisson distribution."""
    x = np.arange(0, 80)
    y = [poisson_distribution(lambda_value, i) for i in x]
    return x, y


def main(args=None):
    output_list = []

    # Validate the input arguments
    lambda_value, error = validate_lambda_value(args)
    if error:
        output_list.append(error + "\nUsage: python script.py <lambda>\n")
        return output_list

    # Generate the Poisson distribution
    x, y = generate_poisson_distribution(lambda_value)

    # Plot the distribution using ASCII
    plot_poisson_ascii(x, y, lambda_value, output_list)

    return output_list


if __name__ == "__main__":
    import sys
    result = main(sys.argv[1:])
    for line in result:
        print(line, end="")
