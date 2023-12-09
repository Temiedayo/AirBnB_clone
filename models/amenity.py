#!/usr/bin/python3
"""defines Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """represent amenity.

    Attributes:
        name (str): Name of amenity.
    """

    name = ""
