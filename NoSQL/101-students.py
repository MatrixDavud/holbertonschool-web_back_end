#!/usr/bin/env python3
"""Mongodb collection modifying with pymongo."""
from pymongo import MongoClient


def top_students(mongo_collection):
    """Returns all students sorted by average score descending."""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
