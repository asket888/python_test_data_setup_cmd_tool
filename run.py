import os
import sys

from termcolor import colored

from statements.create_statements import create_project_with_flights, create_flight_in_existed_project
from statements.delete_statements import delete_project_with_flights, delete_one_flight


def _display_title_bar():
    os.system('clear')
    print("**************************************************")
    print("***  Welcome to APPLICATION TESTING data tool  ***")
    print("**************************************************")


def _get_env_choice():
    print(colored("\nPlease choose env where you would like to run script", 'yellow'))
    print("[1] DEV")
    print("[2] UAT")
    print("[3] LOCALHOST")
    print("[q] Quit")
    choice = input(colored("\nType your choice here: ", 'yellow'))

    if choice == '1':
        env = "DEV"
    elif choice == '2':
        env = "UAT"
    elif choice == '3':
        env = "LOCALHOST"
    elif choice == 'q':
        print(colored("\nScrew you guys I'm going home!\n", 'red'))
        sys.exit()
    else:
        print(colored("\nThis choice is not available. Try ones again, please\n", 'red'))
        sys.exit()

    return env.upper()


def _get_action_choice():
    os.system('clear')
    print(colored("\nPlease choose an Action you would like to perform", 'yellow'))
    print("[1] Create new Project with several Flights")
    print("[2] Create new Flight in already existed Project")
    print("[3] Delete Project with all Flights")
    print("[4] Delete one Flight from Project")
    print("[q] Quit")

    return input(colored("\nType your choice here: ", 'yellow'))


def run_app():
    _display_title_bar()
    env = _get_env_choice()
    choice = _get_action_choice()

    if choice == '1':
        flight_quantity = int(input(colored("\nHow many flights would you like to add to the project? ", 'yellow')))
        print(colored(create_project_with_flights(env, flight_quantity), 'green'))

    elif choice == '2':
        project_id = str(input(colored("\nType ID of the project where to add your flight? ", 'yellow')))
        print(colored(create_flight_in_existed_project(env, project_id), 'green'))

    elif choice == '3':
        project_id_list = [int(x) for x in input(colored("\nType ID(s) of the project(s) you would like to delete? ",
                                                         'yellow')).split(',')]
        for project_id in project_id_list:
            print(colored(delete_project_with_flights(env, project_id), 'green'))

    elif choice == '4':
        flight_id_list = [int(x) for x in input(colored("\nType ID(s) of the flight(s) you would like to delete? ",
                                                        'yellow')).split(',')]
        for flight_id in flight_id_list:
            print(colored(delete_one_flight(env, flight_id), 'green'))

    elif choice == 'q':
        print(colored("\nScrew you guys I'm going home!\n", 'red'))
        sys.exit()
    else:
        print(colored("\nThis choice is not available. Try ones again, please\n", 'red'))
        run_app()


if __name__ == '__main__':
    run_app()
