import unittest

from vacation_driving_planner import VacationDrivingPlanner


class TestVacationDrivingPlanner(unittest.TestCase):
    mock_api_key = 'mockapikey'

    def test_get_origin_cities_default_returns_cities(self):
        vdp = VacationDrivingPlanner(self.mock_api_key, load_from_origin='default', load_from_dest='default')
        default_cities = vdp.get_origin_cities()
        self.assertEqual(default_cities, ['Lakeland, Florida', 'Cary, North Carolina'])

    def test_get_destination_cities_default_returns_cities(self):
        vdp = VacationDrivingPlanner(self.mock_api_key, load_from_origin='default', load_from_dest='default')
        default_cities = vdp.get_destination_cities()
        self.assertEqual(default_cities, ['Virginia Beach, Virginia', 'Atlanta, Georgia'])

    def test_filter_driving_with_no_filter_returns_original_results(self):
        vdp = VacationDrivingPlanner(self.mock_api_key, load_from_origin='default', load_from_dest='default')
        # technically driving_results will be an array of objects
        # but this test doesn't care a driving result object looks like
        driving_results = ['goober1', 'goober2', 'goober3']
        expected_filtered_driving_results = driving_results.copy()
        original_results_len = len(driving_results)

        filtered_driving_results = vdp.filter_driving_results(driving_results)
        self.assertEqual(len(filtered_driving_results), original_results_len)
        self.assertEqual(filtered_driving_results, expected_filtered_driving_results)

    def test_get_driving_distances(self):
        pass


if __name__ == '__main__':
    unittest.main()
