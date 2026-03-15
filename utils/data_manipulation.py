```json
{
    "utils/data_manipulation.py": {
        "content": "
import logging
from typing import List, Dict
from bardeen import Bardeen
from helicone import Helicone
from motionplanning import MotionPlanning
from googlecalendar import GoogleCalendar
from hubspot import HubSpot

def non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for the given data.

    Args:
        data (List[float]): The input data.

    Returns:
        float: The non-stationary drift index.
    """
    try:
        logging.info('Calculating non-stationary drift index')
        return sum(data) / len(data)
    except ZeroDivisionError:
        logging.error('Cannot calculate non-stationary drift index for empty data')
        return 0.0

def stochastic_regime_switch(data: List[float], threshold: float) -> bool:
    """
    Determine if a stochastic regime switch has occurred based on the given data and threshold.

    Args:
        data (List[float]): The input data.
        threshold (float): The threshold value.

    Returns:
        bool: True if a stochastic regime switch has occurred, False otherwise.
    """
    try:
        logging.info('Checking for stochastic regime switch')
        return any(x > threshold for x in data)
    except Exception as e:
        logging.error(f'Error checking for stochastic regime switch: {e}')
        return False

def integrate_google_calendar_with_hubspot(calendar: GoogleCalendar, hubspot: HubSpot) -> None:
    """
    Integrate Google Calendar with HubSpot.

    Args:
        calendar (GoogleCalendar): The Google Calendar instance.
        hubspot (HubSpot): The HubSpot instance.
    """
    try:
        logging.info('Integrating Google Calendar with HubSpot')
        calendar.connect(hubspot)
    except Exception as e:
        logging.error(f'Error integrating Google Calendar with HubSpot: {e}')

def automate_tasks_with_bardeen(bardeen: Bardeen, tasks: List[Dict]) -> None:
    """
    Automate tasks using Bardeen.

    Args:
        bardeen (Bardeen): The Bardeen instance.
        tasks (List[Dict]): The tasks to automate.
    """
    try:
        logging.info('Automating tasks with Bardeen')
        for task in tasks:
            bardeen.automate_task(task)
    except Exception as e:
        logging.error(f'Error automating tasks with Bardeen: {e}')

def simulate_rocket_science() -> None:
    """
    Simulate the 'Rocket Science' problem.
    """
    try:
        logging.info('Simulating Rocket Science problem')
        # Create instances of the required classes
        bardeen = Bardeen()
        helicone = Helicone()
        motion_planning = MotionPlanning()
        google_calendar = GoogleCalendar()
        hubspot = HubSpot()

        # Integrate Google Calendar with HubSpot
        integrate_google_calendar_with_hubspot(google_calendar, hubspot)

        # Automate tasks with Bardeen
        tasks = [
            {'task': 'Task 1', 'description': 'This is task 1'},
            {'task': 'Task 2', 'description': 'This is task 2'}
        ]
        automate_tasks_with_bardeen(bardeen, tasks)

        # Calculate non-stationary drift index
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        non_stationary_drift_index_value = non_stationary_drift_index(data)
        logging.info(f'Non-stationary drift index: {non_stationary_drift_index_value}')

        # Check for stochastic regime switch
        threshold = 3.0
        stochastic_regime_switch_value = stochastic_regime_switch(data, threshold)
        logging.info(f'Stochastic regime switch: {stochastic_regime_switch_value}')
    except Exception as e:
        logging.error(f'Error simulating Rocket Science problem: {e}')

if __name__ == '__main__':
    simulate_rocket_science()
",
        "commit_message": "feat: implement specialized data_manipulation logic"
    }
}
```