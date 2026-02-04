from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append({"text": task, "done": False})
        return redirect("/")
    return render_template("index.html", tasks=tasks)

@app.route("/done/<int:task_id>")
def done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
