
# Motivation Tracker

## Overview

Welcome to **Motivation Tracker** – your trusty sidekick in the battle against procrastination and motivational slumps. This command-line tool lets you log your daily activities (both the productive and the less-than-ideal) and calculates a dynamic motivation score based on their immediate and ongoing impacts.

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## How It Works

Each activity you log has:
- An **immediate cost** (a quick impact on your motivation)
- An ongoing **deposit** effect that lasts for a set number of days

When you log an activity, the tool:
1. Applies the immediate cost.
2. Calculates the ongoing deposit effect over its active duration.
3. Sums these up to provide your current motivation score.

This balance shows how today's actions shape your future motivation – a nod to traditional hard work with a modern twist.

## Requirements

- **Python 3.7+** (no external libraries needed)
- A terminal or command prompt to run the script

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yashawal/Motivation-Tracking-System-w-APK-.git
   cd motivation-tracker
   ```
2. **Run the script:**
   ```bash
   python3 motivation_tracker.py
   ```

## Usage

Once you run the script, you'll see a simple menu:

1. **Log Positive Activity:**  
   Record activities like "Deep Work Session" or "Morning Routine" to boost your motivation.
2. **Log Negative Activity:**  
   Log activities such as "Gaming Marathon" or "Social Media Binge" to see their impact.
3. **View Current Status:**  
   Check your total motivation score along with active effects.
4. **View Available Activities:**  
   See a list of all activities, complete with costs, deposits, and duration details.
5. **Exit:**  
   Quit the application (your progress is saved!).

Simply enter the number corresponding to your choice.

## Customization

Want to personalize your experience?  
- Open the `motivation_tracker.py` file.
- Update the `positive_activities` and `negative_activities` dictionaries with your own activities and values.

Feel free to tweak the parameters to best suit your journey toward a more motivated you.

## Contributing

We’re all about progress—both personal and project-based.  
If you have ideas to improve Motivation Tracker or want to add new features:
- Fork the repository.
- Make your changes.
- Submit a pull request.

Your contributions are always welcome, blending timeless tradition with forward-thinking innovation.

## License

This project is licensed under the [MIT License](LICENSE).

---

Embrace the journey of self-improvement—one logged activity at a time. While our traditions from the past have paved the way, the choices we make today set the course for the future. Happy tracking!
