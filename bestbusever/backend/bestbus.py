from bestbusever.backend.bus_route import BusRoute
from bestbusever.frontend.menu import Menu


class BestBusCompany:

    def __init__(self):
        self._routes: dict[int, BusRoute] = {}

    def start_route(self, line_number, origin, destination, list_of_stops):
        new_route = BusRoute(line_number, origin, destination, list_of_stops)
        if line_number not in self._routes:
            self._routes[line_number] = new_route
        else:
            print("This line number already exits")
        return self._routes

    def delete_ride(self, delete):
        if delete in self._routes:
            del self._routes[delete]

    def update_route_info(self, line_to_update, origin, destination, list_of_stops):
        if line_to_update not in self._routes:
            raise Exception("This line number does not exists")
        self._routes[line_to_update] = BusRoute(line_to_update, origin, destination, list_of_stops)
        # new_route = self._routes
        return self._routes



    def __repr__(self):
        return f"{self._routes}"

