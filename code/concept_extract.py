import spacy
import os

# Load NLP model
nlp = spacy.load("en_core_web_sm")

input_path = "transcripts/lecture_text.txt"

# Check file exists
if not os.path.exists(input_path):
    print(" Transcript file not found")
    exit()

# Read transcript
with open(input_path, "r") as f:
    text = f.read()

doc = nlp(text)

# Extract meaningful concepts
concepts = set()

for token in doc:
    if token.pos_ in ["NOUN", "PROPN"]:
        concepts.add(token.text)

# Convert to list
concepts = list(concepts)

# Save output
os.makedirs("outputs", exist_ok=True)

with open("outputs/concepts.txt", "w") as f:
    for c in concepts:
        f.write(c + "\n")

# Display nicely
print("\n Extracted Concepts:\n")
for c in concepts:
    print("•", c)

print("\n Concepts saved to outputs/concepts.txt")