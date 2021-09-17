# Rooms for Rent in Singapore
> The purpose of this project is to create a web app listing affordable rooms for rent in Singapore. The rental lists are scraped from [roomz.asia](https://sg.roomz.asia/), and the data is updated daily. Web app can be found [here](https://share.streamlit.io/titus-chin/rooms-for-rent-in-singapore/main/app.py).
#### -- Project Status: Active

## Table of Contents
* [Project Structure](#project-structure)
* [Methods Used](#methods-used)
* [Technologies](#technologies)
* [Project Description](#project-description)
* [Results](#results)
* [Getting Started](#getting-started)
* [Contact](#contact)
* [License](#license)

## Project Structure
    ├── .circleci          <- Configuration file used by CircleCI for continuous integration
    |
    ├── conf
    │   ├── credentials    <- YAML files containing credentials and environment variables
    │   └── parameters     <- YAML files containing parameters for source code
    | 
    ├── data               <- Data for use in this project
    │
    ├── docs               <- Documentation for source code generated by Sphinx
    │
    ├── references         <- Data dictionary, manuals, and all other explanatory materials
    │
    ├── src                <- Source code for use in this project
    │   └── data           <- Scripts to download or generate data
    |
    ├── tests              <- Unit tests for source code, folder structure mirrowing src folder
    |
    ├── .gitignore         <- Tell Git which files to ignore
    |
    ├── .pre-commit-config.yaml  <- Configuration file for pre-commit hooks
    |
    ├── LICENSE            <- License for this project
    |
    ├── Makefile           <- Makefile with commands like `make test` or `make docs`
    |
    ├── README.md          <- The top-level README for this project
    |
    ├── activate.sh        <- Shell script to activate the virtual environment
    |
    ├── app.py             <- Script to create a web app
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    |
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    |
    └── tox.ini            <- Tox file with settings for running tox for unit testing

## Methods Used
- Web Scraping

## Technologies
- Python - version 3.8.10
    - Scrapy - version 2.5.0
    - Streamlit - version 0.88.0
- GNU Make - version 4.2.1
- Streamlit Cloud
- AWS S3

## Project Description
People will need to rent rooms for various reasons, some need a room for a new job, some need a room to further study, and I might need a room too if I choose to work in Singapore. Therefore, I decided to create a web app to list down affordable rooms for rent in Singapore to help those who need a room in Singapore including future me.

The rental lists are scraped from [roomz.asia](https://sg.roomz.asia/). According to its website, roomz.asia is a property rental website with hundreds of new listings added daily. Because of that, the data of this web app will be updated daily. To make it simple, I will only scrape the location of the rooms, the headline and the link of rental posts, and rent per month in Singapore Dollar (S$). Data dictionary can be found [here](references/data_dictionary.md).

Scrapy is used to scrape the rental lists, and streamlit is used to create a web app. The web app is deployed on Streamlit Cloud with AWS S3 as its data storage.

## Results
A simple web app can be found [here](https://share.streamlit.io/titus-chin/rooms-for-rent-in-singapore/main/app.py). The rental lists covered 5 areas in Singapore namely West Singapore, Central Singapore, East Singapore, Northeast Singapore and North Singapore. These data are sorted by rent in ascending order. The rent is ranging from S$200 per month to S$1500 per month. All rental lists will be updated daily.

To improve this web app, we can include other attributes such as does the room has private bathroom? So far this web app is just focusing on single rooms for rent, not including whole units for rent yet. Therefore, this is another thing we can consider in the future.

## Getting Started
Follow [these instructions](references/getting_started.md) to reproduce this project.

## Contact
Created by [Titus Chin](https://www.linkedin.com/in/titus-chin-jun-hong/), feel free to contact me!

## License
This project is open source and available under the [MIT License](LICENSE).
