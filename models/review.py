#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Review Module

This Module inherits from Base model class.
Review Module contains all data to be assigned
to the reviews.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class

    Attributes:
        place_id (str): The UUID of the Place the Review belongs to
        user_id (str): The UUID of the User that made the review
        text (str): The message the User wrote about the Place

    """
    place_id = ''
    user_id = ''
    text = ''
