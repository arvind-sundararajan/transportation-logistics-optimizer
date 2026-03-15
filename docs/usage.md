# Stochastic Scheduling Optimization Engine Usage
## Introduction
The Stochastic Scheduling Optimization Engine is designed to optimize truck and ground transportation logistics. This document provides a step-by-step guide on how to use the engine.
## Prerequisites
* Python 3.9 or higher
* Docker installed on the system
## Installation
To install the engine, run the following command:
```bash
pip install -r requirements.txt
```
## Running the Engine
To run the engine, use the following command:
```bash
docker-compose up -d
```
## Configuration
The engine can be configured using environment variables. The following variables are available:
* `OPTIMIZATION_ALGORITHM`: The optimization algorithm to use (default: `genetic`)
* `POPULATION_SIZE`: The population size for the optimization algorithm (default: `100`)
* `GENERATIONS`: The number of generations for the optimization algorithm (default: `100`)
## Example Use Case
To optimize a transportation schedule, create a JSON file with the following format:
```json
{
    "vehicles": [
        {
            "id": 1,
            "capacity": 10
        },
        {
            "id": 2,
            "capacity": 15
        }
    ],
    "packages": [
        {
            "id": 1,
            "weight": 5
        },
        {
            "id": 2,
            "weight": 10
        }
    ]
}
```
Then, run the engine with the following command:
```bash
docker-compose run --rm engine python optimize.py example.json
```
## Output
The engine will output the optimized schedule in the following format:
```json
{
    "schedule": [
        {
            "vehicle_id": 1,
            "package_id": 1
        },
        {
            "vehicle_id": 2,
            "package_id": 2
        }
    ]
}
```
