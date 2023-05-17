# Load and import each JSON data file
for filename in os.listdir(data_path):
    if filename == 'model_comparisons.json':
        with open(os.path.join(data_path, filename)) as f:
            data = json.load(f)
            # Transform the data to match the model comparison structure
            transformed_data = [{
                'model': model,
                'details': details
            } for model, details in data.items()]
            collection.insert_many(transformed_data)
