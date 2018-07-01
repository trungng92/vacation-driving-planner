# Get a list of popular cities
# Get starting city(s) (and weights for starting cities)
# get driving distances from starting city(s) to list of popular cities
## Initial algorithm just checks starting city to all dest cities (but can be optimized to search through less cities)
# filter items by criteria (e.g. max driving distance)
## Map with overlayed colors to see max driving distances for each starting city


### Deploy with Django https://www.djangoproject.com/start/
### Use GIS services with Django https://docs.djangoproject.com/en/2.0/ref/contrib/gis/
### Deploy Django on aws https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
### Deploy Django on Heroku https://devcenter.heroku.com/articles/getting-started-with-python#introduction

import datetime
import pprint
from typing import Callable, List
import os

import googlemaps

API_KEY = os.environ['GOOGLE_MAPS_API_KEY']

gmaps = googlemaps.Client(key=API_KEY)

now = datetime.date
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="driving")
print(directions_result)
pp = pprint.pprint(directions_result)

class VacationDrivingPlanner:
    def __init__(self):
        self.driving_filter = DrivingFilter()

    def get_destination_cities(self):
        pass

    def get_origin_cities(self):
        pass

    def get_driving_distances(self, origin_cities: 'OriginCities', destination_cities: 'DestinationCities') -> List:
        pass

    def filter_driving_results(self, driving_results: List) -> List:
        pass

    def map_driving_results(self, driving_results: List):
        pass

class DestinationCities:
    def get_cities(self):
        pass

    def _get_cities_from_csv(self):
        pass

class OriginCities:
    def get_cities(self):
        pass

    def _get_cities_from_csv(self):
        pass

class DrivingFilter:
    def __init__(self):
        self.filters = {}

    def add_filter(self, filter_name: str, filter_func: Callable[[List], List]):
        pass

    def remove_filter(self, filter_name: str):
        delattr(self.filters, filter_name)

    def run(self, driving_results: List) -> List:
        for filter_name, filter_func in self.filters.items():
            print("running filter", filter_name)
            driving_results = filter_func(driving_results)

        return driving_results
