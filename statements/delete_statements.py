from sql import flight_sql
from sql import project_sql
from utils.db_executor import execute_select_sql_query, execute_non_select_sql_query, get_connection


def delete_project_with_flights(env, project_id):
    conn = get_connection(env)
    project_name = execute_select_sql_query(conn, project_sql.SELECT_PROJECT_NAME_BY_ID
                                            .format(project_id=project_id))[0]
    all_project_flights_id = execute_select_sql_query(conn, project_sql.SELECT_ALL_PROJECT_FLIGHTS_ID
                                                      .format(project_id=project_id))[0].split()
    for flight_id in all_project_flights_id:
        delete_one_flight(env, flight_id)

    execute_non_select_sql_query(conn, project_sql.DELETE_PROJECT_BY_ID.format(project_id=project_id))

    return f"\nYour project '{project_name}' was deleted successfully\n"


def delete_one_flight(env, flight_id):
    conn = get_connection(env)
    flight_name = execute_select_sql_query(conn, flight_sql.SELECT_FLIGHT_NAME_BY_ID.format(flight_id=flight_id))[0]
    execute_non_select_sql_query(conn, flight_sql.DELETE_FLIGHT_BY_ID.format(flight_id=flight_id))

    return f"\nYour flight '{flight_name}' was deleted successfully\n"
