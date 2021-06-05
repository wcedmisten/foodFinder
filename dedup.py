#!/usr/bin/env python3
import json

new_dict = {}

# all recipes retrieved from https://archive.org/download/recipes-en-201706/
with open("/home/wedmisten/Downloads/allrecipes-recipes.json") as dataset:
    with open("dedup.json", "w") as dup:
        for i, line in enumerate(dataset.readlines()):
            data = json.loads(line)
            # pprint.pprint(data)
            if data["title"] == "Johnsonville® Three Cheese Italian Style Chicken Sausage Skillet Pizza":
                continue

            dup.write(line)