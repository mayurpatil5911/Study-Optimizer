🧠 Study Scheduler CLI
A simple Python command-line tool that helps you create a personalized study plan by distributing study hours across multiple days based on task importance and deadlines.

📌 Features
✅ Priority-based task scheduling

⏳ Deadline-aware study hour distribution

🗓 Balanced daily workload (customizable limit)

👨‍💻 User-friendly command-line interface

📂 How It Works
You input the number of topics to study.

For each topic, you provide:

Name

Importance (high/medium/low)

Deadline (in YYYY-MM-DD format)

Estimated study hours

The script calculates:

A priority score (based on importance and deadline proximity)

Distributes your study time across available days

Ensures no more than 4 hours (default) of study per day

Finally, it prints a readable, day-by-day study plan.

💻 Installation
Make sure Python 3 is installed on your machine.

Clone the repo or just download the script:

bash
Copy
Edit
git clone https://github.com/yourusername/study-scheduler.git
cd study-scheduler
▶️ Usage
Run the script using:

bash
Copy
Edit
python study_planner.py
Then follow the prompts in your terminal.

Example:

bash
Copy
Edit
How many subjects/topics do you want to plan? 2
Topic name: Math
Importance (high/medium/low): high
Deadline (YYYY-MM-DD): 2025-04-16
Estimated hours to study: 6
...
Output:

yaml
Copy
Edit
🗓 Study Plan:

📅 Monday, 2025-04-14
  - Math: 2 hour(s)

📅 Tuesday, 2025-04-15
  - Math: 2 hour(s)

📅 Wednesday, 2025-04-16
  - Math: 2 hour(s)
⚙️ Configuration
You can customize the maximum daily study limit by changing this line in allocate_schedule():

python
Copy
Edit
def allocate_schedule(tasks, daily_limit=4):
Change 4 to any number of hours that fits your daily schedule.

🚨 Notes
Ensure deadlines are in the future.

Inputs must match the required formats (especially date and importance).

Priority scores affect the scheduling:

High importance = +2

Medium = +1

Due today or overdue = +3

Due within 2 days = +2

Due within 5 days = +1

📄 License
This project is open-source under the MIT License.

🤝 Contributing
Pull requests and suggestions are welcome! Feel free to fork and enhance the planner.
