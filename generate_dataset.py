import random
import pandas as pd

positive = [
    "I love this", "Amazing product", "Very happy", "Excellent",
    "Fantastic experience", "Superb", "Great quality", "Highly recommend"
]

negative = [
    "I hate this", "Very bad", "Terrible", "Worst experience",
    "Disappointing", "Poor quality", "Not worth it", "Awful"
]

neutral = [
    "It is okay", "Average", "Nothing special", "Fine",
    "Not bad", "Neutral feeling", "Okay product", "Decent"
]

data = []

for _ in range(350):
    data.append([random.choice(positive), "positive"])
    data.append([random.choice(negative), "negative"])
    data.append([random.choice(neutral), "neutral"])

df = pd.DataFrame(data, columns=["text", "label"])
df.to_csv("data.csv", index=False)

print("1000+ dataset generated successfully!")
