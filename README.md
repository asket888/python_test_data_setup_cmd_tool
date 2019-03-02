# Kevin-testing-data-tool:
This console application helps to manage entities right from DB (GUI and API mode available).

# Setup
1. git clone git@github.com:asket888/python-app-testing-tool.git
2. goto `config.json.example` and add actual passwords for all tested environments
3. rename `config.json.example` to `config.json` or use

# Command line Execution (GUI mode):
1. navigate to project directory
2. run `pipenv install --dev --system` to setup all necessary dependencies from Pipfile.lock
3. run `pipenv shell` to be able use all pipenv dependencies from terminal
4. to run application use command `$ python run.py`

# Command line Execution (One line node):
1. navigate to project directory
2. run `pipenv install --dev --system` to setup all necessary dependencies from Pipfile.lock
3. run `pipenv shell` to be able use all pipenv dependencies from terminal
4. - create project:
    `invoke create-project`
    `invoke create-project --env=DEV --flight-num=3 --flight-network=InDisplayYouTube`
   - create flight:
    `invoke create-flight --project-id=789`
    `invoke create-flight --env=DEV --project-id=789 --flight-network=InDisplayYouTube`
   - delete project:
    `invoke delete-project --project-id=789`
    `invoke delete-project --env=DEV --project-id=789`
   - delete flight:
    `invoke delete-flight --flight-id=1234`
    `invoke delete-flight --env=DEV --flight-id=1234`