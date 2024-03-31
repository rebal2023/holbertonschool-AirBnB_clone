#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""User Module

This Module contains the user information
and is inherited from Base Module

"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class

    Attributes:
        email (str): The User email
        password (str): The User password
        first_name (str): The first name of the User
        last_name (str): The last name of the User

    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
