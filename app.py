# Import flask framework
from flask import Flask, request

# Create instance of Flask application
app = Flask(__name__)

# In memory store of tasks (reset when the server restarts)
tasks = [
    {"id": 1, "title": "Write documentation"}, 
    {"id": 2, "title": "Review pull requests"} 
] 
# Server controls Ids
next_task_id = 3

# Get all tasks: GET /tasks
@app.route("/tasks", methods=["GET"]) 
def get_tasks():
    return tasks

# Get task by ID: GET /tasks/:id
@app.route("/tasks/<int:task_id>", methods=["GET"]) 
def get_task(task_id): 
    for task in tasks: 
        # Task is found
        if task["id"] == task_id: 
            return task 
    # If we get here, no task was found
    return {"error": "Task not found"}, 404

# Create a new task: POST /tasks 
@app.route("/tasks", methods=["POST"]) 
def create_task(): 
    # Defining next_task_id as global, so Python doesn't create a local variable
    global next_task_id
    
    # Extract body from request
    data = request.get_json() 
 
    # Validate input (body or title are empty)
    if not data or "title" not in data: 
        return {"error": "Missing required field: title"}, 400 
 
    # Create new task ID 
    new_id = next_task_id 
 
    task = { 
        "id": new_id, 
        "title": data["title"] 
    } 
    
    # Incremint Id to avoid conflicts 
    next_task_id += 1
    
    # Add new task to task list
    tasks.append(task) 
 
    return task, 201

# Update a task by ID: PUT /tasks/:id
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    data = request.get_json()

    # Validate input
    if not data or "title" not in data:
        return {"error": "Missing required field: title"}, 400

    for task in tasks:

        # Task found, update it
        if task["id"] == task_id:
            task["title"] = data["title"]
            return task

    # If we get here, no task was found
    return {"error": "Task not found"}, 404

# Delete a task by ID: DELETE /tasks/:id
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    for task in tasks:

        # Task found, remove it
        if task["id"] == task_id:
            tasks.remove(task)
            return "", 204

    # If we get here, no task was found
    return {"error": "Task not found"}, 404

# Run the server
if __name__ == "__main__":
    app.run(port=5000)