import random


def approximate_pi_loop(n_iter: int) -> float:
    """
    A function to approximate $\pi$ using a Monte Carlo method

    Args:
        n_iter: int - Number of interations to run 
    Out:
        Approximation of pi: float
    """

    # generate a list of length `n_iter`, with random numbers between 0 and 1
    xs = [random.random() for _ in range(n_iter)]
    ys = [random.random() for _ in range(n_iter)]

    # initialise the count, this keeps track of points within the 1/4 circle
    count = 0
    for i in range(n_iter):
        if (xs[i] ** 2 + ys[i] ** 2) ** 0.5 <= 1.0:
            count += 1

    return count * 4 / n_iter


def approximate_pi_comp(n_iter: int) -> float:
    """
    A function to approximate $\pi$ using a Monte Carlo method

    Args:
        n_iter: int - Number of interations to run 
    Out:
        Approximation of pi: float
    """

    # generate a list of length `n_iter`, with random numbers between 0 and 1
    xs = [random.random() for _ in range(n_iter)]
    ys = [random.random() for _ in range(n_iter)]

    count = sum([1 for (x, y) in zip(xs, ys) if (x ** 2 + y ** 2) ** 0.5 <= 1.0])

    return count * 4 / n_iter


def approximate_pi_figure(n_iter: int):
    """
    A function to approximate $\pi$ using a Monte Carlo method

    Args:
        n_iter: int - Number of interations to run 
    Out:
        A tuple containing pi and dictionary containing data to plot
    """

    # make a dictionary to hold the data
    pi_data = {}

    # generate a list of length `n_iter`, with random numbers between 0 and 1
    # and put them into the `pi_data` dictionary
    pi_data["xs"] = [random.random() for _ in range(n_iter)]
    pi_data["ys"] = [random.random() for _ in range(n_iter)]

    # initialise location and count
    location = [""] * n_iter
    count = 0
    for i in range(n_iter):
        if (pi_data["xs"][i] ** 2 + pi_data["ys"][i] ** 2) ** 0.5 <= 1.0:
            location[i] = "in"
            count += 1
        else:
            location[i] = "out"

    # now add location to the dictionary
    pi_data["location"] = location

    return count * 4 / n_iter, pi_data
