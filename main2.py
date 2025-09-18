import requests
import json

def get_search_results(query):
    url = 'https://deepsearch.jina.ai/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer jina_458fd6b9a13a4ad0a8a3fcc41eeee654DFQvgs0dja6RE9aL7bAebvqq1377'
    }
    data = {
        "model": "jina-deepsearch-v1",
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ],
        "stream": False,
        "reasoning_effort": "medium",
        "budget_tokens": 50000
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        json_response = response.json()
        print("Raw response:", json.dumps(json_response, indent=2))  # Debug print
        
        # Process and structure the response
        processed_response = {
            "content": None,
            "citations": [],
            "visitedURLs": json_response.get("visitedURLs", []),
            "readURLs": json_response.get("readURLs", []),
            "numURLs": json_response.get("numURLs", 0),
            "usage": json_response.get("usage", {})
        }
        
        # Handle both response formats
        if "choices" in json_response and json_response["choices"]:
            choice = json_response["choices"][0]
            
            # Handle streaming format (delta)
            if "delta" in choice:
                processed_response["content"] = choice["delta"].get("content")
                processed_response["annotations"] = choice["delta"].get("annotations", [])
            
            # Handle non-streaming format (message)
            elif "message" in choice:
                processed_response["content"] = choice["message"].get("content")
                processed_response["annotations"] = choice["message"].get("annotations", [])
        
        print("Processed response:", json.dumps(processed_response, indent=2))  # Debug print
        return processed_response
    except Exception as e:
        return {"error": str(e)}

