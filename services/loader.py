import json



def load_posts(filename="data/posts.json"):
    
    try:        
        with open(filename, "r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        print(f"Error: {filename} was not found")
        return []

    except json.JSONDecodeError:
        print(f"Error: {filename} contains invalid JSON.")
        return []

