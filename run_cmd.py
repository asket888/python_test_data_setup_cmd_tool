import sys

from statements.create_statements import create_project_with_flights, create_flight_in_existed_project
from statements.delete_statements import delete_project_with_flights, delete_one_flight


def create_project(env='', flights_quantity=''):
    print(create_project_with_flights(env, flights_quantity))


def create_flight(env='', project_id=''):
    print(create_flight_in_existed_project(env, project_id))


def delete_project(env='', project_ids=''):
    project_id_list = [int(x) for x in project_ids.split(',')]
    for project_id in project_id_list:
        print(delete_project_with_flights(env, project_id))


def delete_flight(env='', flight_ids=''):
    flight_id_list = [int(x) for x in flight_ids.split(',')]
    for flight_id in flight_id_list:
        print(delete_one_flight(env, flight_id))


if __name__ == '__main__':
    f = sys.argv[1]
    if f == 'create_project':
        create_project(*sys.argv[2:])
    elif f == 'create_flight':
        create_flight(*sys.argv[2:])
    elif f == 'delete_project':
        delete_project(*sys.argv[2:])
    elif f == 'delete_flight':
        delete_flight(*sys.argv[2:])
    else:
        raise AttributeError("There is no such option like " + f +
                             " create_project, create_flight, delete_project, delete_flight are available")
