#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        user_tasks = []
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        for todo in todos:
            task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }
            user_tasks.append(task_info)
        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
