import pandas as pd
from typing import Dict
from mohaf.auction_mechanisms import (
    MOHAFAuction,
    FirstPriceAuction,
    VickreyAuction,
    HungarianAlgorithm,
    GreedyAuction,
    RandomAuction,
)
from mohaf.scenarios import generate_synthetic_scenario

class ExperimentRunner:
    """Main experiment runner for comparative analysis"""

    def __init__(self):
        self.mechanisms = [
            MOHAFAuction(alpha=0.3, beta=0.3, gamma=0.2, delta=0.2),
            FirstPriceAuction(),
            VickreyAuction(),
            HungarianAlgorithm(),
            GreedyAuction(),
            RandomAuction(),
        ]
        self.results = {}

    def run_comprehensive_experiments(self):
        """Run comprehensive experiments across different scenarios"""

        print("=" * 80)
        print("STARTING COMPREHENSIVE AUCTION MECHANISM EXPERIMENTS")
        print("=" * 80)

        scenarios = [
            {"name": "balanced", "n_resources": 50, "n_requests": 30},
            {"name": "high_demand", "n_resources": 40, "n_requests": 60},
            {"name": "low_resource", "n_resources": 25, "n_requests": 40},
            {"name": "large_scale", "n_resources": 100, "n_requests": 80},
            {"name": "small_scale", "n_resources": 20, "n_requests": 15},
        ]

        for scenario in scenarios:
            print(f"\nRUNNING SCENARIO: {scenario['name'].upper()}")
            print("-" * 60)

            # Generate scenario data
            resources, requests = generate_synthetic_scenario(
                n_resources=scenario['n_resources'],
                n_requests=scenario['n_requests'],
                scenario_type=scenario['name'],
            )

            scenario_results = {}

            # Run each mechanism
            for mechanism in self.mechanisms:
                print(f"\nTesting {mechanism.name}...")

                try:
                    # Run auction
                    result = mechanism.run_auction(resources.copy(), requests.copy())

                    # Calculate metrics
                    metrics = mechanism.calculate_metrics(result)

                    scenario_results[mechanism.name] = {
                        'metrics': metrics,
                        'raw_result': result,
                    }

                    # Print immediate results
                    print(f"   Efficiency: {metrics['allocation_efficiency']:.3f}")
                    print(f"   Revenue: ${metrics['revenue']:.2f}")
                    print(f"   Satisfaction: {metrics['satisfaction_rate']:.3f}")
                    print(f"   Utilization: {metrics['resource_utilization']:.3f}")
                    print(f"   Time: {metrics['execution_time']:.4f}s")
                    print(f"   Fairness: {metrics['fairness_index']:.3f}")

                except Exception as e:
                    print(f"   Error running {mechanism.name}: {str(e)}")
                    scenario_results[mechanism.name] = {
                        'metrics': {k: 0 for k in ['allocation_efficiency', 'revenue', 'satisfaction_rate',
                                                  'resource_utilization', 'execution_time', 'communication_overhead', 'fairness_index']},
                        'raw_result': {'allocations': [], 'error': str(e)}
                    }

            self.results[scenario['name']] = scenario_results

            # Show scenario summary
            self._print_scenario_summary(scenario['name'], scenario_results)

        # Final comprehensive analysis
        self._generate_comprehensive_analysis()

    def _print_scenario_summary(self, scenario_name: str, results: Dict):
        """Print summary for a scenario"""
        print(f"\nSCENARIO SUMMARY: {scenario_name.upper()}")
        print("-" * 50)

        # Sort mechanisms by allocation efficiency
        sorted_mechanisms = sorted(results.items(),
                                 key=lambda x: x[1]['metrics']['allocation_efficiency'],
                                 reverse=True)

        print("RANKING BY ALLOCATION EFFICIENCY:")
        for i, (name, result) in enumerate(sorted_mechanisms, 1):
            efficiency = result['metrics']['allocation_efficiency']
            revenue = result['metrics']['revenue']
            satisfaction = result['metrics']['satisfaction_rate']
            print(f"{i:2d}. {name:20s} | Eff: {efficiency:.3f} | Rev: ${revenue:7.2f} | Sat: {satisfaction:.3f}")

    def _generate_comprehensive_analysis(self):
        """Generate comprehensive analysis and visualizations"""

        print("\n" + "=" * 80)
        print("COMPREHENSIVE ANALYSIS & RESULTS")
        print("=" * 80)

        # Prepare data for analysis
        analysis_data = []

        for scenario_name, scenario_results in self.results.items():
            for mechanism_name, result in scenario_results.items():
                metrics = result['metrics']
                row = {
                    'scenario': scenario_name,
                    'mechanism': mechanism_name,
                    **metrics
                }
                analysis_data.append(row)

        df = pd.DataFrame(analysis_data)

        # Save raw results
        df.to_csv('auction_experiment_results.csv', index=False)
        print("Raw results saved to 'auction_experiment_results.csv'")

if __name__ == "__main__":
    runner = ExperimentRunner()
    runner.run_comprehensive_experiments()