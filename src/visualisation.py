import matplotlib.pyplot as plt


def plot_simulation(profits, strategy_name):

    plt.figure(figsize=(10,6))

    plt.hist(profits, bins=50)

    plt.title("AI Strategy Profit Simulation")
    plt.xlabel("Net Profit")
    plt.ylabel("Frequency")

    plt.savefig("outputs/profit_distribution.png")

    plt.show()