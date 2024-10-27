# poisson-distributions-visualization

A simple Python tool to visualize Poisson distributions using ASCII art. This project calculates and displays the probability distribution of events for a given average event rate (lambda) using the Poisson formula. It also includes unit tests to ensure reliability.

## Features

- Visualize Poisson distributions in a terminal-friendly format using ASCII art.
- Supports lambda values between 1 and 50.

## Prerequisites

- Python 3.12.7 or higher (recommended)
- `git` and `pip` installed on your system
> **Note**:
> - This project has been tested on macOS and may not work on Windows.  
> - Depending on your environment, you may need to use `python3` and `pip3` instead of `python` and `pip`.


## Installation

```bash
$ git clone https://github.com/kc135st/poisson-distributions-visualization.git
$ cd poisson-distributions-visualization
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Example Usage

To visualize a Poisson distribution with a lambda of `3.0`, use the following command:

```bash
$ python poisson_visualization.py 3
```

## Example Output

- The numeric value after `|` is the calculated probability for each `x`.
- `*` indicates the probability magnitude, where each `*` represents 0.01 of the probability.


```bash
Poisson Distribution (lambda = 3.0):
x= 0 | 0.0498 ****
x= 1 | 0.1494 **************
x= 2 | 0.2240 **********************
x= 3 | 0.2240 **********************
x= 4 | 0.1680 ****************
x= 5 | 0.1008 **********
x= 6 | 0.0504 *****
x= 7 | 0.0216 **
x= 8 | 0.0081 
x= 9 | 0.0027 
x=10 | 0.0008 
x=11 | 0.0002 
x=12 | 0.0000
```

## Testing

The project includes tests to validate input and ensure the correct calculation of Poisson probabilities. You can run the tests using the following command:

```bash
$ coverage run -m unittest test_script.py 
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

To generate the report, use:

```bash
$ coverage report -m                     
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
poisson_visualization.py      49      4    92%   77-81
test_script.py                42      0   100%
--------------------------------------------------------
TOTAL                         91      4    96%
```

## Tested Environment

This project has been tested on the following environment:


- **Operating System**
  - ProductName:    macOS
  - ProductVersion: 13.0
  - BuildVersion:   22A380
- **Python**
  - Python 3.12.7


## References

Poisson distribution formula

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$
