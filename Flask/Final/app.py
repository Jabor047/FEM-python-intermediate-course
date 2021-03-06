from flask import Flask, render_template, request
from repos.api import repos_with_most_stars
from repos.exceptions import GitHubApiException

app = Flask(__name__)
available_langugaes = ["Python", "JavaScript", "Ruby", "Java"]

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        selected_languages = available_langugaes
    if request.method == 'POST':
        selected_languages = request.form.getlist("languages")

    results = repos_with_most_stars(selected_languages)

    return render_template('index.html', selected_languages=selected_languages,
                           available_langugaes=available_langugaes, results=results)

@app.errorhandler(GitHubApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)
