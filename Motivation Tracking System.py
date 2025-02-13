import json
from datetime import datetime, timedelta
import os

class MotivationTracker:
    def __init__(self):
        self.data_file = "motivation_data.json"
        self.positive_activities = {
            "Deep Work Session": {"cost": -8, "deposit": 5, "duration_days": 5},
            "Morning Routine": {"cost": -6, "deposit": 4, "duration_days": 3},
            "Weekly Social Connection": {"cost": -3, "deposit": 4, "duration_days": 4},
            "Learning New Skill": {"cost": -7, "deposit": 3, "duration_days": 6},
            "Nature Walk": {"cost": -2, "deposit": 3, "duration_days": 2},
            "Creative Project Work": {"cost": -5, "deposit": 4, "duration_days": 4},
            "Evening Planning": {"cost": -2, "deposit": 3, "duration_days": 2},
            "Declutter Space": {"cost": -4, "deposit": 2, "duration_days": 3},
            "Digital Detox": {"cost": -6, "deposit": 4, "duration_days": 3},
            "Meal Prep Sunday": {"cost": -9, "deposit": 5, "duration_days": 6}
        }
        
        self.negative_activities = {
            "Gaming Marathon": {"cost": 8, "deposit": -3, "duration_days": 3},
            "Social Media Binge": {"cost": 5, "deposit": -2, "duration_days": 2},
            "YouTube Rabbit Hole": {"cost": 6, "deposit": -2, "duration_days": 2},
            "Junk Food Feast": {"cost": 7, "deposit": -4, "duration_days": 2},
            "Skipping Exercise": {"cost": 4, "deposit": -3, "duration_days": 3},
            "Late Night Netflix": {"cost": 6, "deposit": -5, "duration_days": 1},
            "Task Procrastination": {"cost": 5, "deposit": -4, "duration_days": 4},
            "Impulsive Shopping": {"cost": 8, "deposit": -3, "duration_days": 5}
        }
        
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.activity_log = {datetime.fromisoformat(k): v for k, v in data['activity_log'].items()}
        else:
            self.activity_log = {}

    def save_data(self):
        with open(self.data_file, 'w') as f:
            data = {
                'activity_log': {k.isoformat(): v for k, v in self.activity_log.items()}
            }
            json.dump(data, f, indent=2)

    def log_activity(self, activity_name, activity_type="positive"):
        activities = self.positive_activities if activity_type == "positive" else self.negative_activities
        if activity_name not in activities:
            print(f"Activity '{activity_name}' not found in {activity_type} activities.")
            return

        now = datetime.now()
        activity_data = activities[activity_name]
        self.activity_log[now] = {
            "name": activity_name,
            "type": activity_type,
            "cost": activity_data["cost"],
            "deposit": activity_data["deposit"],
            "duration_days": activity_data["duration_days"]
        }
        self.save_data()
        print(f"Logged {activity_name} at {now}")

    def calculate_current_motivation(self):
        now = datetime.now()
        total_motivation = 0
        active_effects = []

        for timestamp, activity in self.activity_log.items():
            # Calculate immediate cost impact
            total_motivation += activity["cost"]
            
            # Calculate ongoing deposits
            end_date = timestamp + timedelta(days=activity["duration_days"])
            if now <= end_date:
                days_active = (end_date - now).days
                deposit_impact = activity["deposit"] * days_active
                total_motivation += deposit_impact
                
                active_effects.append({
                    "activity": activity["name"],
                    "type": activity["type"],
                    "remaining_days": days_active,
                    "daily_impact": activity["deposit"]
                })

        return total_motivation, active_effects

    def print_status(self):
        motivation, effects = self.calculate_current_motivation()
        print("\nCurrent Motivation Status:")
        print(f"Total Motivation Score: {motivation}")
        
        if effects:
            print("\nActive Effects:")
            for effect in effects:
                print(f"- {effect['activity']}: {effect['daily_impact']} per day for {effect['remaining_days']} more days")
        else:
            print("\nNo active effects")

def main():
    tracker = MotivationTracker()
    
    while True:
        print("\n1. Log Positive Activity")
        print("2. Log Negative Activity")
        print("3. View Current Status")
        print("4. View Available Activities")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            print("\nAvailable Positive Activities:")
            for i, activity in enumerate(tracker.positive_activities.keys(), 1):
                print(f"{i}. {activity}")
            activity_num = int(input("\nEnter activity number: ")) - 1
            activity_name = list(tracker.positive_activities.keys())[activity_num]
            tracker.log_activity(activity_name, "positive")
            
        elif choice == "2":
            print("\nAvailable Negative Activities:")
            for i, activity in enumerate(tracker.negative_activities.keys(), 1):
                print(f"{i}. {activity}")
            activity_num = int(input("\nEnter activity number: ")) - 1
            activity_name = list(tracker.negative_activities.keys())[activity_num]
            tracker.log_activity(activity_name, "negative")
            
        elif choice == "3":
            tracker.print_status()
            
        elif choice == "4":
            print("\nPositive Activities:")
            for name, data in tracker.positive_activities.items():
                print(f"- {name}: Cost {data['cost']}, Deposit {data['deposit']} for {data['duration_days']} days")
            print("\nNegative Activities:")
            for name, data in tracker.negative_activities.items():
                print(f"- {name}: Cost {data['cost']}, Deposit {data['deposit']} for {data['duration_days']} days")
                
        elif choice == "5":
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()