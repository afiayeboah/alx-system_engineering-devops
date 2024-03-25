#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


def export_to_json(user_id, username, todos):
    data = {"USER_ID": []}
    for todo in todos:
        data["USER_ID"].append({
            "task": todo["title"],
            "completed": todo["completed"],
            "username": username
        })
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    export_to_json(user_id, username, todos)
    print(f"Data exported to {user_id}.json")
