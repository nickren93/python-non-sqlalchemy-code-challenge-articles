class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Names must be of type str, and must be longer than 0 characters!")
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        raise ValueError("Title cannot be changed once the article is instantiated!")
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Author must be of type Author!")   
        
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Magazine must be of type Magazine!") 
        
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Names must be of type str, and must be longer than 0 characters!")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        raise ValueError("Name cannot be changed once the author is instantiated!")
            

    def articles(self):
        #pass
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        #pass
        all_magazines_list = [article.magazine for article in self.articles()]
        unique_magazines_list = list(set(all_magazines_list))
        return unique_magazines_list

    def add_article(self, magazine, title):
        #pass
        return Article(self, magazine, title)

    def topic_areas(self):
        #pass
        if self.articles():
            all_magazines_list = [article.magazine for article in self.articles()]
            all_categories = [magazine.category for magazine in all_magazines_list]
            unique_categories = list(set(all_categories))
            return unique_categories
        else:
            return None

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Names must be of type str, and must be lbetween 2 and 16 characters, inclusive!")
        
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be of type str, and must be longer than 0 characters!")

    def articles(self):
        #pass
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        #pass
        all_authors_list = [article.author for article in self.articles()]
        unique_authors_list = list(set(all_authors_list))
        return unique_authors_list

    def article_titles(self):
        #pass
        if self.articles():
            return [article.title for article in self.articles()]
        else:
            return None

    def contributing_authors(self):
        #pass
        all_authors_list = [article.author for article in self.articles()]
        two_articles_authors = [author for author in all_authors_list if all_authors_list.count(author)>=2]
        if two_articles_authors:
            return two_articles_authors
        else:
            return None
        
    @classmethod
    def top_publisher(cls):
        top_magazine = None
        top_articles = 0

        for magazine in cls.all:
            if len(magazine.articles()) > top_articles:
                top_articles = len(magazine.articles())
                top_magazine = magazine

        return top_magazine