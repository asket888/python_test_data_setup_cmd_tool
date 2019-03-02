import re

from datetime import datetime, timedelta


def get_date_in_future(num_days):
    date = re.sub('\s(.*)', ' 00:00:00', str(datetime.now() + timedelta(days=num_days)))
    return date
