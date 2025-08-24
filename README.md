# MOHAF: Multi-Objective Hierarchical Auction Framework

## Overview
This repository provides the implementation and supporting materials for the paper:

"MOHAF: A Multi-Objective Hierarchical Auction Framework for Scalable and Fair Resource Allocation in IoT Ecosystems"

MOHAF is a distributed resource allocation mechanism for heterogeneous IoT environments.  
It combines hierarchical clustering, submodular optimization, and dynamic pricing to achieve:

- Efficient allocation of resources in large-scale IoT ecosystems  
- Joint optimization of cost, energy efficiency, quality of service (QoS), and fairness  
- Theoretical guarantees with a (1 - 1/e) approximation ratio  
- Perfect fairness across participants (Jain’s Index = 1.000 in experiments)  

We provide code, experimental setup, and references to enable reproducibility and extension of this work.

---
## Repository Contents

```
MOHAF-Resource-Allocation
├─ .gitignore
├─ LICENSE
├─ MOHAF.ipynb
├─ README.md
├─ docs
│  ├─ index.md
│  ├─ mohaf_paper.pdf
│  └─ usage.md
├─ examples
│  ├─ analyze_results.ipynb
│  └─ run_experiments.py
├─ mohaf
│  ├─ __init__.py
│  ├─ auction_mechanisms.py
│  ├─ core.py
│  ├─ scenarios.py
│  └─ utils.py
├─ pyproject.toml
├─ requirements.txt
└─ tests
   ├─ __init__.py
   ├─ test_auction_mechanisms.py
   └─ test_core.py
```
---

## Usage
### Prerequisites
- Python 3.9+  
- Jupyter Notebook or JupyterLab  

### Steps
1. Install Python and Jupyter  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the notebook:  
   ```bash
   jupyter notebook MOHAF.ipynb
   ```
4. Modify parameters in the notebook to reproduce experiments or adapt MOHAF to other datasets.  

---

## Dataset
Experiments rely on the publicly available Google Cluster Data: https://github.com/google/cluster-data  

---

## License
This project is licensed under the MIT License.  

---

## Citation
If you use this repository, please cite the associated paper:

```
@misc{Agrawal2025,
  author       = {Agrawal, Kushagra and Goktas, Polat and Bandopadhyay, Anjan, and Ghosh, Debolina and Jena, Junali Jasmine and Gourisaria, Mahendra Kumar},
  title        = {MOHAF: A Multi-Objective Hierarchical Auction Framework for Scalable and Fair Resource Allocation in IoT Ecosystems},
  year         = {2025},
  eprint       = {2508.14830},
  archivePrefix= {arXiv},
  primaryClass = {cs.DC},
  doi          = {10.48550/arXiv.2508.14830},
  url          = {https://arxiv.org/abs/2508.14830}
}
```

---

📌 Repository link: https://github.com/afrilab/MOHAF-Resource-Allocation/tree/main
