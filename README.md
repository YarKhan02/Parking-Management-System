# Parking System with Priority Scheduling

This Python script simulates a parking system using priority scheduling, where cars arrive at gates and are assigned parking slots based on their priority. The script utilizes threading for concurrent execution of car arrival and parking processes.

## Dependencies
- Python 3.x
- `threading` module
- `collections` module
- `time` module

## Usage
1. Ensure you have Python installed on your system.
2. Run the script using the command: `python parking_system.py`

## Description
- The script defines classes and functions to simulate a parking system:
    - `CustomBoundedSemaphore`: A custom class derived from `BoundedSemaphore` to manage parking slots with a maximum value.
    - `Car`: Represents a car with attributes like ID, arrival time, burst time, and priority.
    - `Gate`: Simulates a gate where cars arrive and get processed based on their priority.
    - `ParkingSystem`: Manages the overall parking system, initializes gates, and handles car entry.
    - `priority_scheduling`: Implements priority scheduling logic to determine the next car to be processed.
- Cars arrive randomly at gates with randomly generated attributes such as ID, arrival time, burst time, and priority.
- Threads are used to simulate concurrent processing of cars at different gates.
- Parking slots are managed using a bounded semaphore to ensure a maximum number of cars can be parked simultaneously.
- Cars are processed based on their priority, and the process involves acquiring locks to access shared resources (parking slots).
- The script runs for a fixed duration, simulating the arrival of cars over time.

## Functionality
1. Cars arrive at gates randomly with randomly generated attributes.
2. Cars are processed based on their priority and availability of parking slots.
3. Threads are used for concurrent execution of car processing.
4. Parking slots are managed using a bounded semaphore to limit the number of cars that can be parked simultaneously.
5. Cars are processed sequentially based on their priority, ensuring fairness in resource allocation.

## Contributors
- Wali Yar Khan - yarkhan025@gmail.com

Feel free to contribute to the project by forking the repository and submitting a pull request with your changes.
