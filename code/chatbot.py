import os

# Load story
story_path = "outputs/story.txt"

if not os.path.exists(story_path):
    print("❌ Story not found. Run visual_story.py first.")
    exit()

with open(story_path, "r") as f:
    story = f.read()

def chatbot():
    print("🤖 AI Tutor Ready! Ask about Virtualization (type 'exit' to stop)\n")

    while True:
        q = input("You: ").lower()

        if q == "exit":
            break

        # Relevant topic keywords
        if any(word in q for word in ["virtualization", "virtual machine", "vm", "server", "cloud"]):

            if "virtualization" in q:
                print("Bot: Virtualization allows multiple virtual machines to run on a single physical server.")

            elif "vm" in q or "virtual machine" in q:
                print("Bot: A Virtual Machine is like a separate computer running inside a physical server.")

            elif "server" in q:
                print("Bot: A physical server provides CPU, memory, and storage resources.")

            elif "cloud" in q:
                print("Bot: Cloud computing uses virtualization to efficiently share resources.")

            elif "benefit" in q or "advantage" in q:
                print("Bot: Benefits include better resource utilization, cost reduction, flexibility, and scalability.")

            else:
                print("Bot: This is related to virtualization. Here's a simple explanation:\n")
                print(story[:250], "...")

        else:
            print("Bot: ❌ This question is outside the lecture topic. Please ask about virtualization or cloud computing.")

chatbot()