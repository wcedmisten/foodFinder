#!/usr/bin/env python3
import json
import pprint
import subprocess
import sys

from progress.bar import Bar
from progress.spinner import Spinner


def scrape_all_recipes():
    bar = Bar('Loading recipes', max=91465)

    recipe_list = []
    
    with open("dedup.json") as dataset:
        for i, line in enumerate(dataset.readlines()):
            data = json.loads(line)

            recipe_list.append(data)

            bar.next()

    bar.finish()

    return recipe_list

recipes = scrape_all_recipes()

def cleanUnicode(s):
    """
    Replace unicode fractions with ascii representation

    '⅛' => '1/8'
    """

    unicode_map = {
        # fractions
        '⅛': '1/8',
        '⅜': '3/8',
        '⅝': '5/8',
        '⅞': '7/8',
        '⅙': '1/6',
        '⅚': '5/6',
        '⅕': '1/5',
        '⅖': '2/5',
        '⅗': '3/5',
        '⅘': '4/5',
        '¼': '1/4',
        '¾': '3/4',
        '⅓': '1/3',
        '⅔': '2/3',
        '½': '1/2',
        '™': '',
        '®': '',
        '©': '',
        '…': '',
        '’': "'",
        '‘': "'",
        '”': '"',
        '“': '"',
        'à': 'a',
        'â': 'a',
        'É': 'E',
        'è': 'e',
        'é': 'e',
        'ñ': 'n',
        'ú': 'u',
    }

    for f_unicode, f_ascii in unicode_map.items():
        s = s.replace(f_unicode, ' ' + f_ascii)

    return s

# write an empty file
f = open("input.txt", "w")
f.close()

# recipes = recipes[:10000]

bar = Bar('Writing input file', max=91465)
for i, recipe in enumerate(recipes):
    bar.next()
    with open("input.txt", "a") as f:
        recipe['ingredients'] = [cleanUnicode(ingredient) for ingredient in recipe['ingredients']]
        f.write('\n'.join(recipe['ingredients']) + '\n')
bar.finish()

print("Parsing input file.")
command = subprocess.run(['docker', 'run', '--mount', 'type=bind,source=/home/wedmisten/foodFinder/input.txt,target=/input/input.txt,readonly', 'wedmisten/ingredients-tagger'], capture_output=True)

print("Loading parsed output.")
ingredients = command.stdout
parsed = json.loads(ingredients)

bar = Bar('Removing HTML Tags', max=222034267)
# remove random HTML data
for ingedient in parsed:
    bar.next()
    del ingedient['display']
bar.finish()

bar = Bar('Writing enriched recipes', max=91465)
parsed_idx = 0
for i, recipe in enumerate(recipes):
    bar.next()
    recipe['parsed_ingredients'] = []
    for _ in range(len(recipe['ingredients'])):
        recipe['parsed_ingredients'].append(parsed[parsed_idx])
        parsed_idx += 1

bar.finish()

print("Writing enriched data")
with open("enriched_recipes.json", "w") as f:
    json.dump(recipes, f, indent=2)