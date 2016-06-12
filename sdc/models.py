""" Silver Dollar City models """


class RideWaitTime():
    """ the current wait time for a given ride """
    def __init__(self, ride_name, wait_available, wait_time_minutes):
        """
        :type ride_name: str
        :type wait_available: bool
        :type wait_time_minutes: int
        """
        self.ride_name = ride_name
        self.wait_available = wait_available
        self.wait_time_minutes = wait_time_minutes
