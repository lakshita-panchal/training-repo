import json

mock_json_response = """
{
    "userId": 1,
    "id": 1,
    "title": "Practice Task Complete",
    "completed": true
}
"""

try:
    data = json.loads(mock_json_response)
    
    print("Success! Offline JSON Data inspected:")
    print(f"User ID: {data['userId']}")
    print(f"Title:   {data['title']}")
    print(f"Status:  {data['completed']}")

except Exception as e:
    print(f"An error occurred while parsing JSON: {e}")

