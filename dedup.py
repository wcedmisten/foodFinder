import json

new_dict = {}

# all recipes retrieved from https://archive.org/download/recipes-en-201706/
with open("/home/william/Downloads/allrecipes-recipes.json") as dataset:
    with open("dup.json", "w") as dup:
        for i, line in enumerate(dataset.readlines()):
            data = json.loads(line)
            # pprint.pprint(data)
            if data["title"] == "Johnsonville® Three Cheese Italian Style Chicken Sausage Skillet Pizza":
                continue

            dup.write(line)