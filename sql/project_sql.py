# queries to manage projects from DB
INSERT_PROJECT_BY_NAME = """
            INSERT INTO project 
            (organization_id, 
            account_id, 
            name, 
            advertiser_id)
            VALUES 
            (3,
            (SELECT id FROM account WHERE name = '{account_name}'),
            '{project_name}',
            (SELECT id FROM advertiser WHERE account_id = (SELECT id FROM account WHERE name = '{account_name}')));
            """

UPDATE_PROJECT_SYNC_STATE = """
            UPDATE project SET sync_state = 'READY' WHERE id = '{project_id}';
            """

SELECT_NEXT_PROJECT_ID = """
            SELECT nextval(pg_get_serial_sequence('project', 'id'));
            """

SELECT_PROJECT_ID_BY_NAME = """
            SELECT id FROM project 
            WHERE name = '{project_name}';
            """

SELECT_PROJECT_NAME_BY_ID = """
            SELECT name FROM project 
            WHERE id = '{project_id}';
            """

SELECT_ALL_PROJECT_FLIGHTS_ID = """
            SELECT array_to_string(array(SELECT id FROM flight 
            WHERE project_id = '{project_id}'), ' ');
            """

DELETE_PROJECT_BY_ID = """
            DELETE FROM project
            WHERE id = '{project_id}';
            """
