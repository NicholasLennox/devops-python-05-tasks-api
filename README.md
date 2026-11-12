# PriceFixers Task API

This repository contains a small **task tracking API** used in the DevOps course scenario for *PriceFixers*.

Jim wanted to better understand how backend services and APIs work before introducing larger infrastructure and cloud platforms. Instead of immediately adopting a full project management system, he asked Alice to build a small internal API that exposes task data to other applications.

This API demonstrates the core ideas behind web services:

* servers that run continuously
* HTTP request–response communication
* REST-style CRUD endpoints
* JSON data exchange

The implementation is intentionally simple and stores tasks **in memory** so that the focus remains on understanding how APIs behave.

## Important Note About Data Storage

Tasks are stored **in memory** using a Python list.

This means:

* tasks exist only while the server is running
* restarting the server will reset the task list

This is acceptable for learning and prototyping. Later lessons introduce persistent storage so that data survives server restarts.

## Running the Server

Start the API server with:

```bash
python app.py
```

The server will start on:

```
http://localhost:5000
```

## API Endpoints

### Get All Tasks

```
GET /tasks
```

Returns all tasks currently stored in memory.

Example:

```bash
curl -i http://localhost:5000/tasks
```

### Get Task by ID

```
GET /tasks/{id}
```

Returns a single task.

Example:

```bash
curl -i http://localhost:5000/tasks/1
```

If the task does not exist, the server returns:

```
404 Not Found
```

### Create Task

```
POST /tasks
```

Creates a new task.

Example:

```bash
curl -i -X POST http://localhost:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title": "Prepare release notes"}'
```

Response:

```
201 Created
```

### Update Task

```
PUT /tasks/{id}
```

Updates an existing task.

Example:

```bash
curl -i -X PUT http://localhost:5000/tasks/1 \
-H "Content-Type: application/json" \
-d '{"title": "Write better documentation"}'
```

### Delete Task

```
DELETE /tasks/{id}
```

Removes a task.

Example:

```bash
curl -i -X DELETE http://localhost:5000/tasks/1
```

Successful deletion returns:

```
204 No Content
```

## Example Task Structure

Tasks are represented as simple JSON objects:

```json
{
  "id": 1,
  "title": "Write documentation"
}
```

## Why This API Exists

This project exists purely for learning purposes in the DevOps course.

It demonstrates how:

* a Python program can act as a web server
* APIs expose functionality to other systems
* HTTP methods map to CRUD operations
* backend services communicate using JSON

Later lessons will expand this example by introducing:

* Automated testing
* Persistent storage
* Containerization
* CI/CD pipelines
* Cloud deployment
