import random
import matplotlib.pyplot as plt


def monty_hall(switch=True):
    """
    Simulate the Monty Hall problem.

    Parameters:
    switch (bool, optional): Indicates whether the player switches their door (True) or stays with their original choice (False). Default is True.

    Returns:
    bool: True if the player wins (i.e., the car is behind the player's door), and False otherwise.
    """
    doors = [0, 1, 2]
    car = random.choice(doors)
    player = random.choice(doors)
    goat = None
    for door in doors:
        if door != car and door != player:
            goat = door
            break
    if switch:
        doors.remove(goat)
        player = doors[0]

    return player == car


results = [monty_hall(switch=True) for i in range(1000)]
win_rate = results.count(True) / len(results)
results_stay = [monty_hall(switch=False) for i in range(1000)]
win_rate_stay = results_stay.count(True) / len(results_stay)


plt.bar(["Wins with switch", "Wins without switch"], [
        win_rate, win_rate_stay], color=["green", "blue"], width=0.4)
plt.title("Monty Hall Problem Results")
plt.ylabel("Win Rate (normalized)")
plt.show()
