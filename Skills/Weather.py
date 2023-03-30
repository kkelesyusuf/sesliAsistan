import os

import requests

class Weather:
    def __init__(self):
        self.TOKEN=os.environ.get("WEATHER_TOKEN")

