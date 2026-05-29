from pathlib import Path

from flask import Flask, abort, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resume")
def resume_download():
    resume_dir = Path(app.root_path) / "resume"
    for filename in ("resume.pdf", "resume"):
        file_path = resume_dir / filename
        if file_path.exists():
            return send_from_directory(resume_dir, filename, as_attachment=True)
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
