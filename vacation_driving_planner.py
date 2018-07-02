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

import pprint
from typing import Callable, List
import os

import googlemaps


class VacationDrivingPlanner:
    def __init__(self, gmaps_api_key: str, load_from_origin: str='default', load_from_dest: str='default'):
        self.gmaps_api_key = gmaps_api_key
        self.driving_filter = DrivingFilter()
        self.origin_cities = OriginCities(load_from_origin)
        self.destination_cities = DestinationCities(load_from_dest)

    def get_origin_cities(self):
        return self.origin_cities.get_cities()

    def get_destination_cities(self):
        return self.destination_cities.get_cities()

    def get_driving_distances(self, origin_cities: List[str], destination_cities: List[str]) -> List:
        driving_results = []

        gmaps_client = googlemaps.Client(key=self.gmaps_api_key)
        for origin_city in origin_cities:
            for destination_city in destination_cities:
                directions_result = gmaps_client.directions(origin_city, destination_city, mode='driving')
                driving_results.append(directions_result)

        return driving_results

    def filter_driving_results(self, driving_results: List) -> List:
        return self.driving_filter.run(driving_results)

    def map_driving_results(self, driving_results: List):
        pass

    def run(self):
        origin_cities = self.get_origin_cities()
        destination_cities = self.get_destination_cities()

        initial_driving_results = self.get_driving_distances(origin_cities, destination_cities)
        final_driving_results = self.filter_driving_results(initial_driving_results)

        pprint.pprint(final_driving_results)


class OriginCities:
    def __init__(self, load_from: str='default'):
        self.city_strategy = None
        if load_from == 'default':
            self.city_strategy = self._get_cities_default
        elif load_from == 'csv':
            self.city_strategy = self._get_cities_from_csv
        else:
            raise RuntimeError("Invalid origin city loader" + str(load_from))

    def get_cities(self) -> List[str]:
        return self._get_cities_default()

    def _get_cities_from_csv(self):
        pass

    def _get_cities_default(self):
        return ['Lakeland, Florida', 'Cary, North Carolina']


class DestinationCities:
    def __init__(self, load_from: str='default'):
        self.city_strategy = None
        if load_from == 'default':
            self.city_strategy = self._get_cities_default
        elif load_from == 'csv':
            self.city_strategy = self._get_cities_from_csv
        else:
            raise RuntimeError("Invalid origin city loader" + str(load_from))

    def get_cities(self) -> List[str]:
        return self._get_cities_default()

    def _get_cities_from_csv(self):
        pass

    def _get_cities_default(self):
        return ['Virginia Beach, Virginia', 'Atlanta, Georgia']


class DrivingFilter:
    def __init__(self):
        self.filters = {}

    def add_filter(self, filter_name: str, filter_func: Callable[[List], List]):
        """Note: You can also override previous filters with this"""
        self.filters[filter_name] = filter_func

    def remove_filter(self, filter_name: str):
        delattr(self.filters, filter_name)

    def run(self, driving_results: List) -> List:
        for filter_name, filter_func in self.filters.items():
            print("running filter", filter_name)
            driving_results = filter_func(driving_results)

        return driving_results


if __name__ == '__main__':
    API_KEY = os.environ['GOOGLE_MAPS_API_KEY']
    vdp = VacationDrivingPlanner(API_KEY)
    vdp.run()
