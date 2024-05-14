#Task 1

def log_activity(activities, durations, new_activity, new_duration):
    activities.append(new_activity)
    durations.append(new_duration)

#Function for showing the different activites
def different_activities_log(activities, durations):
    print("Activity log:")
    for i in range(len(activities)):
        print(f"{activities[i]}: {durations[i]} minutes")

#Lists for activities and durations
activities = ["Dancing", "Swimming", "Biking"]
#Corresponding durations
durations = [10, 20, 15]

#Show the activity log
different_activities_log(activities, durations)


#Task 2

def calculate_calories_burned(duration):
    calories_per_minute = 3.5
    total_calories_burned = duration * calories_per_minute
    return total_calories_burned

duration = 30
calories_burned = calculate_calories_burned(duration)
print(f"Calories burned in {duration} mminutes: {calories_burned} calories.")


#Task 3

def summarize_activities(activities, durations):
    total_calories = 0
    print("Fitness activity for today:")
    for i in range(len(activities)):
        calories = calculate_calories_burned(durations[i])
        total_calories += calories
        print(f"{activities[i]}: {durations[i]} minutes, {calories} calories burned.")
    print(f"Total calories burned today: {total_calories}.")

#Calling the function
summarize_activities(activities, durations)