"""A library that provides a Python interface to the Silver Dollar City API"""


class Api():
    def __init__(self, base_url):
        if base_url is None:
            self.base_url = 'http://brainflo.net/apps/sdc/ride-times/show_times_m.php'
        else:
            self.base_url = base_url