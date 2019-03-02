import logging
import psycopg2

from psycopg2 import extras

from utils.config_util import get_env
from utils.logging_util import logger

logger = logging.getLogger(__name__)


def get_connection(env_name):
    env = get_env(env_name)
    return psycopg2.connect(host=env["db_host"],
                            database=env["db_name"],
                            port=env["db_port"],
                            user=env["db_user"],
                            password=env["db_pswd"])


def execute_non_select_sql_query(conn, sql_query):
    try:
        with conn.cursor() as cur:
            cur.execute(sql_query)
            conn.commit()
            logger.info("DB output: " + str(cur.statusmessage))
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)


def execute_select_sql_query(conn, sql_query):
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(sql_query)
            result = cur.fetchone()
            logger.info("DB output: " + str(cur.statusmessage))
            return result
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
