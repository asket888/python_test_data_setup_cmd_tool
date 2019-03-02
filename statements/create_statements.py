from getpass import getuser

from sql import project_sql, flight_sql
from utils.math_util import get_date_in_future
from utils.db_executor import execute_select_sql_query, execute_non_select_sql_query, get_connection

_ACCOUNT_NAME = "[TEST] Account"

_FLIGHT_NAME_TEMPLATE = "[TEST] FLIGHT_{flight_id}"
_PROJECT_NAME_TEMPLATE = "[TEST] {user_name}_{project_id}"


def create_project_with_flights(env, flights_quantity):
    conn = get_connection(env)
    user_name = getuser().upper()
    project_id = int(execute_select_sql_query(conn, project_sql.SELECT_NEXT_PROJECT_ID)[0]) + 1
    project_name = _PROJECT_NAME_TEMPLATE.format(user_name=user_name,
                                                 project_id=project_id)
    execute_non_select_sql_query(conn,
                                 project_sql.INSERT_PROJECT_BY_NAME.format(account_name=_ACCOUNT_NAME,
                                                                           project_name=project_name))
    for flight in range(int(flights_quantity)):
        create_flight_in_existed_project(env, project_id)

    return f"\nYour project '{project_name}' was generated successfully. Enjoy your testing!\n" \
           f"Direct link: {_get_project_link(env, project_id)}"


def create_flight_in_existed_project(env, project_id):
    conn = get_connection(env)
    flight_id = int(execute_select_sql_query(conn, flight_sql.SELECT_NEXT_FLIGHT_ID)[0]) + 1
    flight_name = _FLIGHT_NAME_TEMPLATE.format(flight_id=flight_id)
    start_date = get_date_in_future(10)
    end_date = get_date_in_future(15)

    execute_non_select_sql_query(conn, flight_sql.INSERT_FLIGHT_WITH_BY_NAME
                                 .format(flight_name=flight_name,
                                         project_id=project_id,
                                         start_date=start_date,
                                         end_date=end_date))

    execute_non_select_sql_query(conn, flight_sql.UPDATE_FLIGHT_CREATIVE_BY_NAME
                                 .format(flight_name=flight_name))

    return f"\nYour flight '{flight_name}' was generated successfully. Enjoy your testing!\n" \
           f"Direct link: {_get_project_link(env, project_id)}"


def _get_project_link(env, project_id):
    if env.upper() == 'DEV' or env.upper() == 'UAT':
        link = f"https://ai-{env}.strikesocial.com/projects/{project_id}\n"
    else:
        link = f"http://localhost:3000/projects/{project_id}\n"
    return link
