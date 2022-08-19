# FoodFinder

Exploratory data analysis of a [dataset](https://archive.org/details/recipes-en-201706)
of 91,000 recipes scraped from allrecipes.com


[ingredient-phrase-tagger](https://github.com/mtlynch/ingredient-phrase-tagger) was used to parse ingredients into
units, quantities, and names.

# Setup

Unpack the compressed JSON file:

```
tar -xvf enriched_recipes.tar
```

# Datasets

`enriched_recipes.json` contains recipe data that has been enriched by
`ingredient-phrase-parser`

`ABBREV.csv` contains data from the [SR28 dataset](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/methods-and-application-of-food-composition-laboratory/mafcl-site-pages/sr11-sr28/) published by the USDA,
which contains the weights/densities of many ingredients.
