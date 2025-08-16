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
- MOHAF.ipynb – Jupyter Notebook implementation of the MOHAF framework  
- requirements.txt – Python dependencies for running the notebook  
- README.md – Documentation  

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
@inproceedings{Agrawal2025,
  title     = {MOHAF: A Multi-Objective Hierarchical Auction Framework for Scalable and Fair Resource Allocation in IoT Ecosystems},
  author    = {Agrawal, K., Goktas, P., Bandopadhyay, A., Ghosh, D., Jasmine, J. & Gourisaria, M. K.},
  year      = {2025}
}
```

---

📌 Repository link: https://github.com/afrilab/MOHAF-Resource-Allocation/tree/main
