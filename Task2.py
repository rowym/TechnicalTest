import json

# Path to the input text file
text_file_path = 'D:\eT3 challenge\image1.txt'
json_file_path = 'D:\eT3 challenge\output.json'

# Readin and extracting the data
with open(text_file_path, 'r') as file:
    text_data = file.read().rstrip('\n')

# Process the data and converting it to the desired JSON format
lines = text_data.split('\n')
annotations = []
current_annotation = None


for line in lines:
    if line.strip():  # Check if the line is not empty
        values = line.split(' ')
        # to make sure that result word is added only once
        if current_annotation is None:
            current_annotation = {
                "result": []
            }
            # adding the numbers in the required format
        annotation = {
            "image_rotation": 0,
            "value": {
                "x": round(float(values[1])*100,5),
                "y": round(float(values[2])*100,5),
                "width": round(float(values[3])*100,5),
                "height": round(float(values[4])*100,5),
                "rotation": 0,
                "rectanglelabels": ["object"]
            }
        }

        current_annotation["result"].append(annotation)

# append the last annotation if it exists
if current_annotation is not None:
    annotations.append(current_annotation)

# Create JSON object
json_data = {
    "annotations": annotations,
    "data": {
        "image": "\/data\/upload\/image1.jpg"
    }
}

# Write JSON data to the output
with open(json_file_path, 'w') as file:
    json.dump(json_data, file, indent=4)
