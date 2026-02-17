"""

Author: Ramtin Loghmani
Assignment: #1

"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool

# Step c: Create a dictionary named workout_stats
# Dictionary with friend names as keys and workout tuples (yoga, running, weightlifting) as values in minutes
workout_stats = {"Alex": (30, 35, 50), "Jamie": (75, 50, 5), "Taylor": (15, 10, 150)}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend in ["Alex", "Jamie", "Taylor"]:
    total = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total


# Step e: Create a 2D nested list called workout_list
# list - 2D nested list containing workout minutes for each friend (rows=friends, columns=activities)
workout_list = [list(workout_stats[friend]) for friend in ["Alex", "Jamie", "Taylor"]]

# Step f: Slice the workout_list
# Slice 1: Extract yoga and running minutes (first 2 columns) for all friends
print("Yoga and Running minutes for all friends:")
yoga_running = [row[:2] for row in workout_list]
print(yoga_running)

# Slice 2: Extract weightlifting minutes (last column) for last two friends
print("\nWeightlifting minutes for last two friends:")
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print(weightlifting_last_two)

# Step g: Check if any friend's total >= 120
print("\nFriends with 120+ total minutes:")
for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
print("\nAvailable friends: Alex, Jamie, Taylor")
user_input = input("\nEnter a friend's name to view their stats: ")
if user_input in ["Alex", "Jamie", "Taylor"]:
    activities = workout_stats[user_input]
    total = workout_stats[f"{user_input}_Total"]
    print(f"{user_input}'s workout minutes:")
    print(f"  Yoga: {activities[0]} minutes")
    print(f"  Running: {activities[1]} minutes")
    print(f"  Weightlifting: {activities[2]} minutes")
    print(f"  Total: {total} minutes")
else:
    print(f"Friend {user_input} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
friends_only = ["Alex", "Jamie", "Taylor"]
highest_friend = max(friends_only, key=lambda f: workout_stats[f"{f}_Total"])
lowest_friend = min(friends_only, key=lambda f: workout_stats[f"{f}_Total"])

print(
    f"\nFriend with highest total: {highest_friend} ({workout_stats[f'{highest_friend}_Total']} minutes)"
)
print(
    f"Friend with lowest total: {lowest_friend} ({workout_stats[f'{lowest_friend}_Total']} minutes)"
)
