# 🚀 Enterprise API Automation Framework

A robust, portfolio-grade API testing framework designed to validate backend services and database operations. Built with Python, this framework executes lightning-fast CRUD operations, parses complex JSON payloads, and integrates seamlessly into a CI/CD pipeline.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **Core Library:** Requests (HTTP Client)
- **Test Runner:** Pytest
- **Reporting:** Allure Reports
- **CI/CD:** GitHub Actions

## ⚙️ Core Architecture & Features
- **Full CRUD Automation:** Automated workflows for `GET` (Read), `POST` (Create), and `DELETE` (Remove) HTTP methods.
- **Data Validation:** Deep JSON payload extraction and exact-match verification.
- **Status Code Assertions:** Built-in safeguards to verify server health (200 OK, 201 Created, 204 No Content).
- **Enterprise Reporting:** Custom Pytest hooks (`conftest.py`) automatically generate environment metadata for Allure dashboards.
- **Cloud-Native CI/CD:** Fully automated YAML pipeline that spins up an Ubuntu server and executes the test suite on every code push in under 15 seconds.

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/TechSathish007/python-api-framework.git](https://github.com/TechSathish007/python-api-framework.git)