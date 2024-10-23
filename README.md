# poisson-distributions-visualization

A simple Python tool to visualize Poisson distributions using ASCII art. This project calculates and displays the probability distribution of events for a given average event rate (lambda) using the Poisson formula. It also includes unit tests to ensure the reliability.

## Features
- Visualize Poisson distributions in a terminal-friendly format using ASCII art.

## Install

```bash
$ pip install -r requirements.txt
```

## Example Usage

To visualize a Poisson distribution with a lambda of `3.0`, use the following command:

```bash
$ python poisson_visualization.py 3

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

You can run the tests using the following command:
```bash
$ coverage run -m unittest test_script.py 

...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

To generate the report, use:
```bash
$ coverage report -m                     
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
poisson_visualization.py      43      4    91%   66-69
test_script.py                49      1    98%   81
--------------------------------------------------------
TOTAL                         92      5    95%
```

## References
Poisson distribution formula

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$
