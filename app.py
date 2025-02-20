import hashlib, os

from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect
)

from articles import Article

app = Flask(__name__)
app.secret_key = "thisisverysecret"

app.secret_key = 'thisisverysecret'

users = {
    "admin": 'dcd2705cf213701be5c5235a69c46fd55f433928772903db679ed6391d1c0795'
}

@app.route("/set-session")
def set_session():
    session["user_id"] = 1
    return "session set"


@app.route("/get-session")
def get_session():
    return f"user_id = {session["user_id"]}"


@app.route("/")
def blog():
    return render_template("blog.html", articles=Article.all())


@app.get("/admin")
def admin_page():
    if 'user' in session:
        return "You are already authenticated"
    return render_template("login.html")


@app.get("/logout")
def logout():
    del session['user']
    return "Logged out!"


@app.post("/admin")
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    if username not in users:
        return render_template("login.html", error='username/password insorrect!')
    
    hashed = hashlib.sha256(password.encode()).hexdigest()

    if users[username] != hashed:
        return render_template("login.html", error='username/password insorrect!')

    session['user'] = username
    
    return "You are now authenticated!"


@app.route("/blog/<slug>")
def atricle(slug: str):
    if slug not in Article.all():
        return "article not found", 404
    article = Article.all()[slug]
    return render_template("article.html", article=article)


@app.get('/publish')
def publish_page():
    if 'user' not in session:
        return redirect('/admin')

    return render_template("publish.html")


@app.post('/publish')
def publishing():
    file_name = request.form["title"]
    content = request.form["content"]

    folder_path = "articles"
    file_path = os.path.join(folder_path, file_name)
    os.makedirs(folder_path, exist_ok=True)
    
    if file_name in os.listdir("articles"):
        return f"Bunday sarlavhali maqola allaqachon mavjud!"

    with open(file_path, "w") as file:
        file.write(content)
    return "Yangi maqola tayyor bo'ldi!"


@app.get('/delete-article')
def delete_page():
    if 'user' not in session:
        return redirect('/admin')
    
    return render_template("delete_article.html")

@app.post('/delete-article')
def delete_article():
    file_name = request.form['title']
    file_path = f"articles/{file_name}"

    if file_name not in os.listdir("articles"):
        return "Bunday sarlavhali maqola mavjud emas!"
    
    os.remove(file_path)
    return "Sarlavha o'chirildi!"


if __name__ == "__main__":
    app.run(port=4200, debug=True)