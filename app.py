from flask import Flask, render_template
import os

app = Flask(__name__)

# Read logs and calculate effectiveness
def read_logs():
    log_file = "logs.txt"
    if not os.path.exists(log_file):
        return []

    tasks = []
    success_count = 0
    failure_count = 0
    total_time = 0

    with open(log_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split("|")
            if len(parts) == 3:
                task, status, time = parts
                execution_time = int(time)
                tasks.append({"task": task, "status": status, "time": execution_time})

                # Effectiveness calculations
                if status.lower() == "success":
                    success_count += 1
                else:
                    failure_count += 1

                total_time += execution_time

    total_tasks = success_count + failure_count
    success_rate = (success_count / total_tasks) * 100 if total_tasks > 0 else 0
    failure_rate = (failure_count / total_tasks) * 100 if total_tasks > 0 else 0
    avg_execution_time = total_time / total_tasks if total_tasks > 0 else 0

    effectiveness = {
        "Success Rate": f"{success_rate:.2f}%",
        "Failure Rate": f"{failure_rate:.2f}%",
        "Average Execution Time": f"{avg_execution_time:.2f} seconds"
    }

    return tasks, effectiveness

@app.route("/")
def dashboard():
    tasks, effectiveness = read_logs()
    return render_template("index.html", tasks=tasks, effectiveness=effectiveness)

if __name__ == "__main__":
    app.run(debug=True)
