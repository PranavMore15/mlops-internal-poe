# MLOps Internal POE - UAT Pipeline

An automated Continuous Integration (CI) and User Acceptance Testing (UAT) pipeline configured locally using **Jenkins**, **Git**, **Pytest**, and automated monitoring reporting.

---

## 🚀 Project Overview
This repository contains a lightweight MLOps pipeline designed to validate code quality through unit testing and generate automated monitoring reports for data drift detection.

## 🛠️ Tech Stack
* **CI/CD Orchestration:** Jenkins (Freestyle Project)
* **Version Control:** Git & GitHub
* **Testing Framework:** Pytest
* **Data Processing & Monitoring:** Python, Pandas, Custom Drift Report Generator
* **Environment:** Windows, Python 3.13

---

## 📂 Repository Structure
```text
├── hello.py              # Core application logic
├── test_hello.py         # Pytest unit test suite
├── monitor.py            # Automated monitoring & HTML report generator
└── README.md             # Project documentation
