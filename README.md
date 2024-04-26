# Satellite Orbit Elements Conversion Toolkit

## Overview
This repository contains a Jupyter notebook and a Docker-compose file designed to facilitate the learning and implementation of satellite orbit element conversions. The focus is on the definition and conversion between Cartesian and Keplerian orbit elements.

## Features
- **Jupyter Notebook**: Includes detailed implementations and explanations on how to define Cartesian and Keplerian orbit elements, as well as how to convert between these two types of orbit elements.
- **Docker Environment**: The provided `docker-compose.yml` file sets up a ready-to-use Docker environment, ensuring that all necessary dependencies are installed and configured correctly to run the notebook.

## Getting Started
To get started with this toolkit, follow these steps:

### Prerequisites
Ensure that you have Docker and Docker-compose installed on your machine. These tools will help you create a containerized environment where the Jupyter notebook can be run without any dependency issues.

### Installation
1. Clone this repository to your local machine:
2. Navigate into the repository directory:
3. Launch the Docker containers:
```shell
docker compose up
```

This command builds and starts the Docker containers defined in the `docker-compose.yml` file.

### Accessing the Notebook
Once the Docker environment is running, access the Jupyter notebook through your web browser:
- Open `http://localhost:8888`
- You will be prompted to enter a token. You can find this token in the terminal output where you executed `docker-compose up`.

## Learning Objectives
- Understand the fundamental concepts of Cartesian and Keplerian orbit elements.
- Learn how to perform conversions between Cartesian and Keplerian orbit elements using Python implementations provided in the Jupyter notebook.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
