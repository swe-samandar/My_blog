from articles import Article
import pytest

@pytest.fixture
def article():
    return Article("Test title")

def test_article_init(article):
    assert article.title == "Test title"
    assert article.content == ""

def test_article_slug(article):
    assert article.slug == "test-title"


def test_article_slug_mock(mocker, article):
    # given
    mock_slugify = mocker.patch('articles.slugify', return_value="test")

    # when
    got = article.slug

    # then
    assert got == "test"
    mock_slugify.assert_called_with("Test title")