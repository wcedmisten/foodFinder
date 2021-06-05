#!/usr/bin/env python3
import json
import pprint
import subprocess
import sys

import nltk 
import re 
import numpy as np 


def scrape_all_recipes():
    recipe_list = []
    
    with open("dedup.json") as dataset:
        for i, line in enumerate(dataset.readlines()):
            data = json.loads(line)

            recipe_list.append(
                {
                    "title": data["title"], "ingredients": data["ingredients"]
                }
            )

            if i % 10000 == 0:
                print(f"{i} / 91000")

    return recipe_list


# def get_real_ingredients():
#     with open("real_ingredients.json") as real:
#         return json.load(real)
#     with open("/home/william/Downloads/ingredients.json") as ingredients_data:
#         data = json.load(ingredients_data)
#         real_ingredients_list = [ingredient["name"].lower() for ingredient in data["tags"]]

#         return real_ingredients_list[:100]

# real_ingredients = get_real_ingredients()

recipes = scrape_all_recipes()
# only run on 10 to test with
recipes = recipes[:10]

for i, recipe in enumerate(recipes[:10]):
    with open("input.txt", "w") as f:
        f.write('\n'.join(recipe['ingredients']) + '\n')
    
    command = subprocess.run(['docker', 'run', '--mount', 'type=bind,source=/home/wedmisten/foodFinder/input.txt,target=/input/input.txt,readonly', 'wedmisten/ingredients-tagger'], capture_output=True)

    sys.stdout.buffer.write(command.stdout)
    sys.stderr.buffer.write(command.stderr)