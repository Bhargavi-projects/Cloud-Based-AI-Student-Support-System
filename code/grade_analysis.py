import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "data/grades.csv"

if not os.path.exists(file_path):
    print(" File not found:", file_path)
    exit()

df = pd.read_csv(file_path)

print("\n Loaded Data:\n")
print(df.head())

# ✅ FIXED COLUMN NAMES
avg_scores = df.groupby("Topic")["Marks"].mean()

print("\n Average Scores:\n")
print(avg_scores)

# Weak concepts (<70 for better demo)
weak = avg_scores[avg_scores < 70]

print("\n Weak Concepts:\n")
if len(weak) == 0:
    print("No weak areas ")
else:
    for concept, score in weak.items():
        print(f"• {concept} (Score: {score})")

# Suggestions
print("\n Suggestions:\n")
for concept in weak.index:
    print(f"→ Revise {concept} using story explanation and chatbot")

# Plot graph
avg_scores.plot(kind="bar")
plt.title("Concept-wise Performance")
plt.ylabel("Marks")
plt.xlabel("Topic")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()