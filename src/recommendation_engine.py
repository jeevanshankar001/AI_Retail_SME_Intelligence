import numpy as np
from src.scoring import calculate_risk_adjusted_score


def generate_strategy_report(results):

    report = []

    for strategy_name in results:

        profits = results[strategy_name]["profits"]

        avg_profit = np.mean(profits)
        worst_case = np.min(profits)
        best_case = np.max(profits)
        volatility = np.std(profits)

        score = calculate_risk_adjusted_score(profits)

        report.append({
            "strategy": strategy_name,
            "avg_profit": avg_profit,
            "worst_case": worst_case,
            "best_case": best_case,
            "volatility": volatility,
            "score": score
        })

    report = sorted(report, key=lambda x: x["score"], reverse=True)

    return report