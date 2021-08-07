import pandas as pd
import json

with open('enriched_recipes.json') as f:
    data = json.load(f)
    df = pd.json_normalize(data, 'parsed_ingredients', meta=['author', 'photo_url', 'prep_time_minutes', 'rating_stars', 'review_count', 'title', 'total_time_minutes', 'url'], record_prefix='ingredient_', errors='ignore')

grouped = df.where(df['rating_stars'] > 0).where(df['review_count'] > 20).groupby(['ingredient_name'])['rating_stars'].mean()