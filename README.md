Motivation Tracker
Welcome to Motivation Tracker – your trusty sidekick in the battle against procrastination and motivational slumps. This command-line tool lets you log your daily activities – both the virtuous and the vice-filled – and calculates a dynamic motivation score based on their immediate and ongoing impacts. It’s the perfect blend of old-school diligence and forward-thinking tech!

Overview
In these fast-paced times, sometimes the best way to achieve greatness is by keeping track of how your actions add up. With Motivation Tracker, you can:

Log Positive Activities: Record productive endeavors like "Deep Work Sessions" or "Morning Routine" to boost your overall motivation.
Log Negative Activities: Admit when you’ve indulged in a "Gaming Marathon" or a "Social Media Binge"—because hey, honesty is the first step to improvement.
Persistent Data: Your logs are saved in a JSON file (motivation_data.json), ensuring your hard-earned motivation score persists even after you shut down the terminal.
Real-Time Feedback: Calculate and view your current motivation score, complete with the daily ongoing effects of your activities.
How It Works
Each activity has an immediate cost and an ongoing deposit that lasts for a specified number of days. When you log an activity, the tool:

Applies the immediate cost to your motivation.
Calculates the ongoing deposit impact over its active duration.
Sums these effects up to provide your current motivation score.
This balance of immediate penalties and future rewards (or penalties) helps you see how your actions today can shape your motivation for tomorrow. It’s as simple as it is effective—just like the methods of yesteryear, but with a 2025 twist.

Requirements
Python 3.7+ (No external libraries required; just the standard library!)
A terminal or command prompt to run the script.
How to Run
Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/motivation-tracker.git
cd motivation-tracker
Run the script:
bash
Copy
Edit
python3 motivation_tracker.py
Usage
When you run the script, you’ll see a simple menu with the following options:

Log Positive Activity: Choose from activities like "Deep Work Session" or "Morning Routine."
Log Negative Activity: Choose from activities like "Gaming Marathon" or "Social Media Binge."
View Current Status: Check out your total motivation score and active effects.
View Available Activities: See a list of all the activities along with their costs, deposits, and duration.
Exit: Close the application (for now—your motivation is forever logged!).
Simply enter the corresponding number to navigate the menu. The interface is straightforward, because sometimes the simplest approach is the best.

Customization
Want to add your own activities or modify the values? Open the motivation_tracker.py file and update the dictionaries for positive_activities and negative_activities as needed. Feel free to tweak the parameters to best suit your personal journey toward greatness.

Contributing
If you have ideas to improve Motivation Tracker (or just want to share your own tips on staying motivated), contributions are warmly welcomed. Fork the repository, make your changes, and submit a pull request. We value tradition, but we’re always open to forward-thinking improvements!

License
This project is licensed under the MIT License.

Embrace the journey of self-improvement, one logged activity at a time. After all, while habits of the past shaped us, the choices we make today propel us into the future. Happy tracking!

