from unittest import TestCase

from road_collisions_base.models.collision import Collisions
from road_collisions_base.models.raw_collision import RawCollision


class LatLngCollision(RawCollision):

    def __init__(self, *args, **kwargs):
        self._lat = kwargs['lat']
        self._lng = kwargs['lng']
        super().__init__(*args, **kwargs)

    @property
    def lat(self):
        return self._lat

    @property
    def lng(self):
        return self._lng


class CollisionsTest(TestCase):

    def test_filter_within_bbox(self):
        collisions = Collisions()

        collisions.append(
            LatLngCollision(lat=0, lng=0)
        )
        collisions.append(
            LatLngCollision(lat=1, lng=1)
        )
        collisions.append(
            LatLngCollision(lat=2, lng=2)
        )

        filtered = collisions.filter_within_bbox(
            {
                'north': -1,
                'south': -1,
                'east': -1,
                'west': -1
            }
        )
        self.assertEqual(len(filtered), 0)

        filtered = collisions.filter_within_bbox(
            {
                'north': 0,
                'south': 0,
                'east': 0,
                'west': 0
            }
        )
        self.assertEqual(len(filtered), 1)

        filtered = collisions.filter_within_bbox(
            {
                'north': 1,
                'south': 0,
                'east': 0,
                'west': 1
            }
        )
        self.assertEqual(len(filtered), 2)

        filtered = collisions.filter_within_bbox(
            {
                'north': 2,
                'south': 0,
                'east': 0,
                'west': 2
            }
        )
        self.assertEqual(len(filtered), 3)
