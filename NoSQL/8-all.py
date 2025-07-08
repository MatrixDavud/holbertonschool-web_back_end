#!/usr/bin/env python3
"""Mongodb collection modifying."""


def list_all(mongo_collection):
    """Return the list of documents."""
    return list(mongo_collection.find())
