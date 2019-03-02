from invoke import task


@task
def create_project(context, env='localhost', flight_num='1'):
    """
    Create new project with several flights on chosen environment
    :param context: invoke context object
    :param env: run on specific environment (DEV, UAT, LOCALHOST); default value = LOCALHOST
    :param flight_num: number of flights added to project; default value = 1
    :keyword: '$ invoke create-project'
    :keyword: '$ invoke create-project --env=DEV --flight-num=3 --flight-network=InDisplayYouTube --add-media-plan'
    """
    invoke_cmd = f'python run_cmd.py create_project {env} {flight_num}'
    context.run(invoke_cmd)


@task
def create_flight(context, env='localhost', project_id=''):
    """
    :param context: invoke context object
    :param env: run on specific environment (DEV, UAT, LOCALHOST); default value = LOCALHOST
    :param project_id: project_id where flight should be added
    :keyword: '$ invoke create-flight --project-id=789'
    :keyword: '$ invoke create-flight --env=DEV --project-id=789 --flight-network=InDisplayYouTube --add-media-plan'
    """
    invoke_cmd = f'python run_cmd.py create_flight {env} {project_id}'
    context.run(invoke_cmd)


@task
def delete_project(context, env='localhost', project_id=''):
    """
    :param context: invoke context object
    :param env: run on specific environment (DEV, UAT, LOCALHOST); default value = LOCALHOST
    :param project_id: project_ids which should be deleted (use comma separator for multiple delete)
    :keyword: '$ invoke delete-project --project-id=1234'
    :keyword: '$ invoke delete-project --env=DEV --project-id=1234,1235,1236'
    """
    invoke_cmd = f'python run_cmd.py delete_project {env} {project_id}'
    context.run(invoke_cmd)


@task
def delete_flight(context, env='localhost', flight_id=''):
    """
    :param context: invoke context object
    :param env: run on specific environment (DEV, UAT, LOCALHOST); default value = LOCALHOST
    :param flight_id: flight_ids which should be deleted (use comma separator for multiple delete)
    :keyword: '$ invoke delete-flight --flight-id=1234'
    :keyword: '$ invoke delete-flight --env=DEV --flight-id=1234,1235,1236'
    """
    invoke_cmd = f'python run_cmd.py delete_flight {env} {flight_id}'
    context.run(invoke_cmd)
