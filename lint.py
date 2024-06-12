import json, os

directory = "languages"

for entry in os.listdir(directory):
    file = os.path.join(directory, entry)

    with open(file, "r") as f:
        content = json.load(f)
     
    # Sort the words, and remove duplicates
    for item in content:
        item["words"] = sorted(set(item["words"]))
    
    # Write the formatted JSON content back to the file
    with open(file, "w") as f:
        json.dump(content, f, indent=2)
