import os
import pytest

def pytest_sessionfinish(session, exitstatus):
    # This automatically builds the environment details for your API report
    os.makedirs("allure-results", exist_ok=True)
    with open("allure-results/environment.properties", "w") as file:
        file.write("Environment=QA-Backend\n")
        file.write("OS=Windows\n")
        file.write("Engineer=Sathish R\n")
        file.write("Framework=Python API Requests\n")