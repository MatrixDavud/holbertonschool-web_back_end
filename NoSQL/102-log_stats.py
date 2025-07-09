#!/usr/bin/env python3
"""Mongodb collection modification with pymongo."""
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client["logs"]
    collection = db["nginx"]
    num_of_logs = len(list(collection.find()))
    method = {"GET": None, "POST": None, "PUT": None, "PATCH": None, "DELETE": None}
    for key, value in method.items():
        method[key] = len(list(collection.find({ "method": key})))
    print(f"{num_of_logs} logs")
    print("Methods:")
    for k, v in method.items():
        print(f"\tmethod {k}: {v}")
    status_check_count = len(list(collection.find({ "method": "GET", "path": "/status"})))
    print(f"{status_check_count} status check")
    pipeline = [
    {
        "$group": {
            "_id": "$ip",
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 10
    }
    ]
    result = list(collection.aggregate(pipeline))
    print("IPs:")
    for i in range(len(result)):
        print(f"\t{result[i]['_id']}: {result[i]['count']}")