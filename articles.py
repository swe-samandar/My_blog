import os
from slugify import slugify

class Article:
    def __init__(self, title):
        self.title = title
        self.load_content()

    @property
    def slug(self):
        return slugify(self.title)
    
    def load_content(self):
        with open(f"articles/{self.title}") as file:
            self.content = file.read()

    @classmethod
    def all(cls):
        titles = os.listdir("articles")
        slug_articles = {}
        for title in titles:
            article = Article(title)
            slug = article.slug
            slug_articles[slug] = article

        return slug_articles