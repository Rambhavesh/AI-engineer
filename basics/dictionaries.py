# Dictionaries - Key Value Pairs

# Single dictionary (one row)
profile = {
    "name": "Rambhavesh",
    "current_role": "SC",
    "target_role": "AI Engineer",
    "skills": "Claude",
    "experience": "fresh"
}

for key, value in profile.items():
    print(f"{key}: {value}")

print("---")

# List of dictionaries (multiple rows - like a table)
profiles = [
    {"name": "rambo",  "role": "AI eng", "city": "Bengaluru"},
    {"name": "rambo2", "role": "AI eng", "city": "Chennai"}
]

for profile in profiles:
    print(f"{profile['name']} - {profile['role']} - {profile['city']}")
