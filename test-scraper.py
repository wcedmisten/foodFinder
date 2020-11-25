import json
import pprint

import nltk 
import re 
import numpy as np 


def scrape_all_recipes():
    recipe_list = []
    
    with open("dup.json") as dataset:
        for i, line in enumerate(dataset.readlines()):
            data = json.loads(line)

            recipe_list.append(
                {
                    "title": data["title"], "ingredients": data["ingredients"]
                }
            )

            if i % 10000 == 0:
                print(f"{i} / 91000")


def get_real_ingredients():
    with open("real_ingredients.json") as real:
        return json.load(real)
    # with open("/home/william/Downloads/ingredients.json") as ingredients_data:
    #     data = json.load(ingredients_data)
    #     real_ingredients_list = [ingredient["name"].lower() for ingredient in data["tags"]]

    #     return real_ingredients_list[:100]

# real_ingredients = get_real_ingredients()


scrape_all_recipes()