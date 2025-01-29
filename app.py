from flask import Flask, render_template, request, session, make_response
from articles import Article

app = Flask(__name__)
app.secret_key = "thisisverysecret"

articles = Article.all()   

@app.route("/set-session")
def set_session():
    session["user_id"] = 1
    return "session set"

@app.route("/get-session")
def get_session():
    return f"user_id = {session["user_id"]}"
    
@app.route("/")
def blog():
    return render_template("blog.html", articles=articles)

@app.route("/first-time")
def first_time():
    if 'seen' not in request.cookies:
        response = make_response('You are new here!')
        response.set_cookie('seen', "1")
        return response
    
    seen = int(request.cookies['seen'])
    response = make_response(f'I have seen you before {seen} times!')
    response.set_cookie(f'seen', str(seen + 1))
    return response

@app.route("/blog/<slug>")
def atricle(slug: str):
    article = articles[slug]
    return render_template("article.html", article=article)

if __name__ == "__main__":
    app.run(port=4200, debug=True)