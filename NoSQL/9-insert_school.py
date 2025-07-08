#!/usr/bin/env python3
"""Mongodb collection modifying."""


def insert_school(mongo_collection, **kwargs):
    """Insert new document and return its id."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
