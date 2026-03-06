import numpy as np
from src.config import MARKET_VOLATILITY_MEAN, MARKET_VOLATILITY_STD
from src.config import INFLATION_MEAN, INFLATION_STD


def run_simulation(strategy):

    base_revenue = strategy["revenue"]
    base_costs = strategy["costs"]
    ai_investment = strategy["ai_investment"]
    productivity_gain = strategy["productivity_gain"]

    market_fluctuation = np.random.normal(
        MARKET_VOLATILITY_MEAN,
        MARKET_VOLATILITY_STD
    )

    inflation_shock = np.random.normal(
        INFLATION_MEAN,
        INFLATION_STD
    )

    revenue = base_revenue * (1 + productivity_gain) * market_fluctuation / inflation_shock

    costs = base_costs + ai_investment

    profit = revenue - costs

    return profit


def monte_carlo_simulation(strategy, simulations=5000):

    profits = []

    for i in range(simulations):

        profit = run_simulation(strategy)
        profits.append(profit)

    return profits