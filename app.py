import time

import yaml

from lib import mod3


# Code here will change quite frequently
def main(event, context):
    print(f"Event: {event}, Context: {context}")
    print(f"Running with yaml version: [{yaml.__version__}]")
    if mod3(int(time.time())):
        raise Exception("Random exception 1/3 of the time")

