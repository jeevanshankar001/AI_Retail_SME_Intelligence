from src.simulation_engine import monte_carlo_simulation
from src.strategies import strategies
from src.visualisation import plot_simulation
from src.recommendation_engine import generate_strategy_report
from src.stress_testing import run_stress_test


def main():

    results = {}

    for strategy_name, strategy_params in strategies.items():

        profits = monte_carlo_simulation(strategy_params)

        results[strategy_name] = {
            "profits": profits
        }

    report = generate_strategy_report(results)

    print("\n----- Strategy Analysis Report -----\n")

    for r in report:

        print("Strategy:", r["strategy"])
        print("Average Profit:", round(r["avg_profit"],2))
        print("Worst Case Profit:", round(r["worst_case"],2))
        print("Best Case Profit:", round(r["best_case"],2))
        print("Volatility:", round(r["volatility"],2))
        print("Score:", round(r["score"],2))
        print()

    best_strategy = report[0]["strategy"]

    print("Recommended Strategy:", best_strategy)

    plot_simulation(results[best_strategy]["profits"], best_strategy)

    stress_profit = run_stress_test(strategies[best_strategy])

    print("\nAverage Stress Test Profit:", round(stress_profit,2))


if __name__ == "__main__":
    main()