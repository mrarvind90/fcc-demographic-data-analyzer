[![freeCodeCamp Social Banner](https://s3.amazonaws.com/freecodecamp/wide-social-banner.png)](https://www.freecodecamp.org/)

<p style="text-align: center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python 3"/></a>
  <a href="https://pandas.pydata.org"><img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/></a>
</p>

# Demographic Data Analyzer
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg" /></a>
<a href="https://github.com/psf/black"><img alt="Code Style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>

A Python program to analyze data from a 1994 census database from University of California, School of Information and Computer Science.

## Technologies Used
- pandas

## Features
Provides an answer for the following questions based on the 1994 census data
- How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
- What is the average age of men?
- What is the percentage of people who have a Bachelor's degree?
- What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
- What percentage of people without advanced education make more than 50K?
- What is the minimum number of hours a person works per week?
- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
- What country has the highest percentage of people that earn >50K and what is that percentage?
- Identify the most popular occupation for those who earn >50K in India.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python 3.10 or higher installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
- Poetry 1.6.1 installed on your system. You can install Poetry from [python-poetry.org](https://python-poetry.org/docs/#installation)

## Installation and Setup
Follow these steps to install and set up Poetry for this project:

1. **Install Poetry**:
   Poetry is a Python package manager that simplifies dependency management and virtual environments. You can install Poetry by following their guide [here](https://python-poetry.org/docs/#installing-with-the-official-installer).
2. Clone the repository
   ```shell
   git clone git@github.com:mrarvind90/fcc-demographic-data-analyzer.git
   ```
3. Change into the Project Directory
   ```shell
   cd fcc-demographic-data-analyzer
   ```
4. Install Dependencies:
   ```shell
   poetry install
   ```
5. Run the Project:
   ```shell
   poetry run python3 main.py 
   ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Code Style
We follow the black code style for this project. You can format your code using:
```shell
black .
```
