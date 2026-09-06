import requests

def test_get_single_user():
    # 1. The exact URL endpoint for User #2
    url = "https://reqres.in/api/users/2"
    
    # 2. Send a GET request to the server
    response = requests.get(url)
    
    # 3. Print the raw data
    print("\nServer Response:")
    print(response.json())
    
    # 4. Verify the server is online and happy
    assert response.status_code == 200
    
    # 5. Extract the JSON payload into a Python variable
    response_body = response.json()
    
    # 6. Dig into the JSON dictionary to grab the first name, and assert it is "Janet"
    actual_first_name = response_body["data"]["first_name"]
    assert actual_first_name == "Janet", f"Expected Janet, but got {actual_first_name}"





def test_create_new_user():
    # 1. The general Users endpoint
    url = "https://reqres.in/api/users"
    
    # 2. The JSON data (payload) we want to send to the server
    payload = {
        "name": "Sathish",
        "job": "Automation Engineer"
    }
    
    # 3. Send a POST request (shipping our payload TO the server)
    response = requests.post(url, json=payload)
    
    # 4. Print the server's reply
    print("\nPOST Response:")
    print(response.json())
    
    # 5. Verify success. In APIs, a 201 Status Code universally means "Created Successfully"
    assert response.status_code == 201
    
    # 6. Verify the server saved our data correctly
    response_body = response.json()
    assert response_body["name"] == "Sathish"
    assert response_body["job"] == "Automation Engineer"




def test_delete_user():
    # 1. Target the specific user we want to delete (User #2)
    url = "https://reqres.in/api/users/2"
    
    # 2. Send a DELETE request to the server
    response = requests.delete(url)
    
    # 3. Print the status code
    print("\nDELETE Status Code:")
    print(response.status_code)
    
    # 4. Verify success. In APIs, a 204 Status Code universally means "No Content" 
    # (Meaning: It was successfully deleted, and the server has nothing else to say)
    assert response.status_code == 204