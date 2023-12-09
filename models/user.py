#!/usr/bin/python3
"""Defines User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent User.

    Attributes:
        email (str): Email of user.
        password (str): Password of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

