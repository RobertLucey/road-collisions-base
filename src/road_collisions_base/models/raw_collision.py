class RawCollision():

    def __init__(self, **kwargs):
        self.data = kwargs

    def is_within(self, bbox):
        return all([
            bbox['north'] >= self.lng,
            bbox['south'] <= self.lng,
            bbox['east'] <= self.lat,
            bbox['west'] >= self.lng
        ])

    @property
    def lat(self):
        raise NotImplementedError()

    @property
    def lng(self):
        raise NotImplementedError()

    @staticmethod
    def parse(data):
        if isinstance(data, RawCollision):
            return data

        return RawCollision(
            **data
        )
