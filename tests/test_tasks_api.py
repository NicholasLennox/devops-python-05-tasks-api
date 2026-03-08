# tests/test_tasks_api.py 
 
def test_get_tasks_returns_200(client): 
   response = client.get("/tasks") 
 
   assert response.status_code == 200