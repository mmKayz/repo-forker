from flask import Flask, render_template, request
from github import Github

app = Flask(__name__)

REPO_CONST = 'mmKayz/repo-forker'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/fork-repo')
def fork_repo():
    token = request.args.get('token')
    g = Github(token)
    user = g.get_user()
    repo = g.get_repo(REPO_CONST)
    test = user.create_fork(repo)
    return 'User: ' + str(user) + 'Repo: ' + str(repo) + ' Result: ' + str(test)


@app.route('/get-link')
def get_link():
    token = request.args.get('token')
    return '<a href="/fork-repo?token=' + str(token) + '" >Click to Fork</a>'


if __name__ == '__main__':
    app.run()
