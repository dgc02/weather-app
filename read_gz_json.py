import gzip
import json

def read_gz_json(file_path):
    # Step 1: Decompress the .gz file and read its contents
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Example usage
file_path = 'C:/Users/Admin/Downloads/city.list.json.gz'  # Replace with your .json.gz file path
data = read_gz_json(file_path)

# Print the JSON data
print(json.dumps(data, indent=2))  # Pretty-print the JSON data

# Example: Access specific data
if isinstance(data, list) and data:
    print(data[0])  # Print the first item in the list
