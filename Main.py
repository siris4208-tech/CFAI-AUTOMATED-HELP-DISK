from collections import deque

# CO1: Class for Hospital Agent
class HospitalBot:
    def __init__(self):

        # Knowledge Representation using Dictionary
        self.rules = {
            "appointment": "You can book appointments at reception.",
            "doctor": "Doctors are available in Cardiology and Pediatrics.",
            "timing": "Hospital timings are 8 AM to 8 PM.",
            "emergency": "Emergency services are available 24/7.",
            "ambulance": "Ambulance service is available 24/7.",
            "blood": "Blood bank services are available.",
            "fees": "Consultation fee starts from Rs.300.",
            "medicine": "Please consult the doctor before taking medicine.",
            "lab": "Lab testing services are available.",
            "canteen": "Hospital canteen is open from 7 AM to 9 PM.",
            "icu": "ICU services are available for critical patients.",
            "scan": "MRI and CT scan facilities are available.",
            "insurance": "Insurance facilities are accepted here.",
            "covid": "COVID vaccination is available.",
            "room": "Both AC and Non-AC rooms are available."
        }

# CO2: BFS Search Concept
def bfs_search(graph, start):

    visited = set()
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            print("Visited:", node)
            visited.add(node)

            for neighbour in graph[node]:
                queue.append(neighbour)

# CO3: Constraint Checking
def check_doctor(day):

    if day == "sunday":
        return "Doctor not available on Sunday."
    else:
        return "Doctor available."

# Chatbot Function
def chatbot():

    bot = HospitalBot()

    print("🏥 Welcome to Hospital Help Desk Chatbot")
    print("Type 'exit' to stop\n")

    while True:

        user = input("You: ").lower()

        # Exit
        if user == "exit":
            print("Bot: Thank you. Stay healthy 😊")
            break

        # Greetings
        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How can I help you?")

        # Thank You
        elif "thank" in user:
            print("Bot: You're welcome 😊")

        # BFS Demo
        elif "search" in user:

            hospital_map = {
                "Reception": ["Doctor Room", "Lab"],
                "Doctor Room": ["Pharmacy"],
                "Lab": ["Scan Room"],
                "Pharmacy": [],
                "Scan Room": []
            }

            bfs_search(hospital_map, "Reception")

        # Constraint Checking
        elif "doctor sunday" in user:
            print("Bot:", check_doctor("sunday"))

        # Rule-Based Questions
        elif user in bot.rules:
            print("Bot:", bot.rules[user])

        # Default
        else:
            print("Bot: Sorry, I did not understand your question.")

# Run Chatbot
chatbot()
