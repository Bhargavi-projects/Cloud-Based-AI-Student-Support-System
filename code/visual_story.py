import os

concept_path = "outputs/concepts.txt"

if not os.path.exists(concept_path):
    print(" Concepts file not found")
    exit()

with open(concept_path, "r") as f:
    concepts = [c.strip() for c in f.readlines()]

# Build meaningful story
story = """
 STORY-BASED EXPLANATION

Imagine a large apartment building .

Earlier, only one family lived in the entire building.
This is like a physical server running a single operating system.

But this wastes space and resources like CPU, memory, and storage.

Now, virtualization comes into the picture.

A smart manager divides the building into multiple smaller apartments.
Each apartment is like a Virtual Machine (VM).

Each VM:
- Has its own operating system
- Runs its own applications
- Works independently

Even though they share the same physical server,
they behave like separate computers.

This improves:
*  Resource Utilization  
*  Cost Efficiency  
* Flexibility  
* Scalability  

This is why cloud computing uses virtualization,
to efficiently serve many users using fewer resources.
"""

# Save story
os.makedirs("outputs", exist_ok=True)

with open("outputs/story.txt", "w") as f:
    f.write(story)

# Display output
print(story)
print("\n Story saved to outputs/story.txt")