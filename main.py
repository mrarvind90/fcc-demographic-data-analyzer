# This entrypoint file to be used in development. Start by reading README.md
from unittest import main

from src import demographic_data_analyzer

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module="tests.test_module", exit=False)
