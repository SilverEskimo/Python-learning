
class ScheduledRide:
    def __init__(self, origin_time, destination_time, driver_name):
        self._origin_time = origin_time
        self._destination_time = destination_time
        self._driver_name = driver_name
        self._id = ""
        self._delays = 0

    def update(self):
        self._delays += 1
        return self._delays


    def __str__(self):
        return f"Id: {self._id}\n"\
               f"Origin Time: {self._origin_time}\n" \
               f"Destination Time: {self._destination_time}\n"\
               f"Delays: {self._delays}\n"

    def __repr__(self):
        return f"Id: {self._id}\n" \
           f"Origin Time: {self._origin_time}\n" \
           f"Destination Time: {self._destination_time}\n" \
           f"Delays: {self._delays}\n"

