import numpy as np


def run_stress_test(strategy):

    base_revenue = strategy["revenue"]
    base_costs = strategy["costs"]
    ai_investment = strategy["ai_investment"]
    productivity_gain = strategy["productivity_gain"]

    recession_factor = 0.85

    revenue = base_revenue * recession_factor * (1 + productivity_gain)

    costs = base_costs + ai_investment

    profit = revenue - costs

    return profit