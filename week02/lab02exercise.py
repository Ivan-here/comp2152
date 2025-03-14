'''
Author: Ivan Barnash
Assignment: #1
'''

gym_member = "Alex Alliton" # str
preferred_weight_kg = 20.5  # float
highest_reps = 25           # int
membership_active = True    # bool

#creating dictionary
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 30),
    "Taylor": (40, 35, 25)
}

total_minutes = {person + "_Total": sum(minutes) for person, minutes in workout_stats.items()}
workout_stats.update(total_minutes)

workout_list = [list(minutes) for person, minutes in workout_stats.items() if "_Total" not in person]

print("\nYoga and running minutes for all people:")
print([row[:2] for row in workout_list])
print("\nWeightlifting minutes for the last two people:")
print([row[2] for row in workout_list[-2:]])

for person, total in workout_stats.items():
    if "_Total" in person and total >= 120:
        print(f"Great job staying active, {person.replace('_Total', '')}!") #removing _Total

person_name = input("Enter a name: ")
if person_name in workout_stats:
    minutes = workout_stats[person_name]
    print(f"Workout minutes for {person_name}: Yoga: {minutes[0]}, Running: {minutes[1]}, Weightlifting: {minutes[2]}")
    print(f"Total workout minutes: {workout_stats[f'{person_name}_Total']}")
else:
    print(f"Person {person_name} not found in the records.")

person_totals = {person: total for person, total in workout_stats.items() if "_Total" in person}
highest = max(person_totals, key=person_totals.get).replace("_Total", "")
lowest = min(person_totals, key=person_totals.get).replace("_Total", "")
print(f"\nA person with highest workout time: {highest}")
print(f"\nA person with lowest workout time: {lowest}")