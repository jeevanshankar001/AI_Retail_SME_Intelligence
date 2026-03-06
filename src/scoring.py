import numpy as np


def calculate_risk_adjusted_score(profits):

    avg_profit = np.mean(profits)
    volatility = np.std(profits)

    if volatility == 0:
        return 0

    score = avg_profit / volatility

    return score