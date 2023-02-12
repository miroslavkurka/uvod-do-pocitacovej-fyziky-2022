def drunk_sailor_simulation():
    """
    Simulates the drunk sailor problem in 1D and returns the number of steps
    needed to reach the shore.

    Returns:
    int: The number of steps needed to reach the shore.
    """
    import random
    steps = 0
    position = 0
    while position < 100:
        steps += 1
        position += random.choice([-1, 1])

    return steps


print(
    "The sailor needed %d steps to reach the shore." %
    drunk_sailor_simulation())
