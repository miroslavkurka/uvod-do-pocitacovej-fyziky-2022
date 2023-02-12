import matplotlib.pyplot as plt


def logistic_bifurcation(r, x0, iterations):
    """
    Plots the Logistic Bifurcation map for the rabbit population example.

    Parameters:
    r (float): the growth rate parameter
    x0 (float): the initial population density
    iterations (int): the number of iterations to compute

    Returns:
    None
    """
    x = [x0]  # Initialize the population list with the initial density

    for i in range(iterations):
        x.append(r * x[-1] * (1 - x[-1]))  # Apply the logistic map formula

    # Plot the population density over time
    plt.plot(range(iterations + 1), x, 'o', markersize=1)
    plt.title("Logistic Bifurcation Map")
    plt.xlabel("Iterations")
    plt.ylabel("Population Density")
    plt.show()


logistic_bifurcation(3.9, 0.2, 500)

logistic_bifurcation(2.9, 0.2, 500)
