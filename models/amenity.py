#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Amenity Module

This Module inherits from Base model class.
Amenity Module contains all data to be assigned
to the Amenities.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class

    Attributes:
        name (str): The Amenity name

    """
    name = ''
