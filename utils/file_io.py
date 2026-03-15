```json
{
    "utils/file_io.py": {
        "content": "
import logging
from typing import List, Dict
from bardeen import Bardeen
from helicone import Helicone
from motionplanning import MotionPlanning
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

def read_non_stationary_drift_index(file_path: str) -> List[float]:
    """
    Reads the non-stationary drift index from a file.

    Args:
    file_path (str): The path to the file containing the non-stationary drift index.

    Returns:
    List[float]: A list of non-stationary drift indices.
    """
    try:
        logging.info(f'Reading non-stationary drift index from {file_path}')
        with open(file_path, 'r') as file:
            non_stationary_drift_index = [float(line.strip()) for line in file]
        return non_stationary_drift_index
    except Exception as e:
        logging.error(f'Error reading non-stationary drift index: {e}')
        return []

def write_stochastic_regime_switch(file_path: str, stochastic_regime_switch: Dict[str, float]) -> None:
    """
    Writes the stochastic regime switch to a file.

    Args:
    file_path (str): The path to the file where the stochastic regime switch will be written.
    stochastic_regime_switch (Dict[str, float]): A dictionary containing the stochastic regime switch.
    """
    try:
        logging.info(f'Writing stochastic regime switch to {file_path}')
        with open(file_path, 'w') as file:
            for key, value in stochastic_regime_switch.items():
                file.write(f'{key}: {value}\n')
    except Exception as e:
        logging.error(f'Error writing stochastic regime switch: {e}')

def integrate_google_calendar_with_hubspot(calendar_id: str, hubspot_api_key: str) -> None:
    """
    Integrates Google Calendar with HubSpot.

    Args:
    calendar_id (str): The ID of the Google Calendar.
    hubspot_api_key (str): The API key for HubSpot.
    """
    try:
        logging.info('Integrating Google Calendar with HubSpot')
        service = build('calendar', 'v3', developerKey='YOUR_API_KEY')
        events = service.events().list(calendarId=calendar_id).execute()
        bardeen = Bardeen()
        for event in events['items']:
            bardeen.create_trello_card(event['summary'], event['description'])
    except HttpError as e:
        logging.error(f'Error integrating Google Calendar with HubSpot: {e}')

def simulate_rocket_science() -> None:
    """
    Simulates the 'Rocket Science' problem.
    """
    try:
        logging.info('Simulating Rocket Science problem')
        motion_planning = MotionPlanning()
        motion_planning.plan_motion()
    except Exception as e:
        logging.error(f'Error simulating Rocket Science problem: {e}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    non_stationary_drift_index = read_non_stationary_drift_index('non_stationary_drift_index.txt')
    logging.info(f'Non-stationary drift index: {non_stationary_drift_index}')
    stochastic_regime_switch = {'regime1': 0.5, 'regime2': 0.3}
    write_stochastic_regime_switch('stochastic_regime_switch.txt', stochastic_regime_switch)
    integrate_google_calendar_with_hubspot('primary', 'YOUR_HUBSPOT_API_KEY')
    simulate_rocket_science()
",
        "commit_message": "feat: implement specialized file_io logic"
    }
}
```