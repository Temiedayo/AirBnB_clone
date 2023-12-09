#!/usr/bin/python3
"""defines Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent place.

    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): name of place.
        description (str): description of  place.
        number_rooms (int): num of rooms of the place.
        number_bathrooms (int): num of bathrooms of the place.
        max_guest (int): maximum num of guests of place.
        price_by_night (int): price by night of the place.
        latitude (float): latitude of place.
        longitude (float): longitude of place.
        amenity_ids (list): list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
