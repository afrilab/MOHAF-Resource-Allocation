
# MOHAF: A Multi-Objective Hierarchical Auction Framework for IoT Resource Allocation

This repository contains the official implementation of the MOHAF research framework, as presented in the paper "Distributed Auction Mechanisms for Resource Coordination in Internet of Things (IoT) Ecosystems: A Novel Multi-Objective Hierarchical Auction Framework (MOHAF)".

This framework provides a comprehensive suite of tools for simulating and evaluating various auction mechanisms for resource allocation in IoT environments. It is designed to be extensible, allowing researchers to easily add new auction mechanisms, scenarios, and metrics.

## Features

- **Comprehensive Simulation Environment:** Simulate complex IoT scenarios with a large number of resources and requests.
- **Extensible Framework:** Easily add new auction mechanisms, scenarios, and performance metrics.
- **Variety of Auction Mechanisms:** Includes implementations of MOHAF, First-Price, Vickrey, Hungarian, Greedy, and Random auctions.
- **In-depth Performance Analysis:** Automatically calculates a wide range of performance metrics, including allocation efficiency, revenue, satisfaction rate, and fairness.
- **Data Visualization:** Generates a variety of plots and charts to help you visualize and understand the results of your experiments.

## Installation

You can install the MOHAF framework directly from this repository using pip:

```bash
pip install git+https://github.com/your-username/Github-MOHAF.git
```

Alternatively, you can clone the repository and install it in editable mode:

```bash
git clone https://github.com/your-username/Github-MOHAF.git
cd Github-MOHAF
pip install -e .
```

## Quickstart

To run the comprehensive experiment suite, simply run the `run_experiments.py` script in the `examples` directory:

```bash
python examples/run_experiments.py
```

This will run all the defined scenarios and save the results to a CSV file named `auction_experiment_results.csv`.

To analyze the results, you can use the `analyze_results.ipynb` notebook in the `examples` directory. This notebook provides a variety of visualizations and statistical analyses to help you understand the performance of the different auction mechanisms.

## Project Structure

```
Github-MOHAF/
├── mohaf/                  # The core MOHAF library
│   ├── __init__.py
│   ├── auction_mechanisms.py # Implementations of all auction mechanisms
│   ├── core.py               # Core data structures and base classes
│   ├── scenarios.py          # Scenario generation tools
│   └── utils.py              # Utility functions
├── tests/                    # Unit tests
├── examples/                 # Example scripts and notebooks
├── docs/                     # Documentation
├── .gitignore
├── pyproject.toml            # Project metadata and dependencies
└── README.md
```

## Contributing

Contributions are welcome! If you would like to contribute to the MOHAF framework, please fork the repository and submit a pull request.

## Citation

If you use this framework in your research, please cite our paper:

```
@inproceedings{your-name-2026-mohaf,
    author    = {Your Name and Co-authors},
    title     = {Distributed Auction Mechanisms for Resource Coordination in Internet of Things (IoT) Ecosystems: A Novel Multi-Objective Hierarchical Auction Framework (MOHAF)},
    booktitle = {Proceedings of the International Conference on Distributed Computing and Intelligent Technology (ICDCIT)},
    year      = {2026}
}
```
