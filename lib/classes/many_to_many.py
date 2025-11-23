#   AUTHOR CLASS

class Author:
    def __init__(self, name):
        # We store the real name in _name because we want to control changes
        self._name = None
        
        # This calls the setter below to validate the name
        self.name = name

    @property
    def name(self):
        # Getter: returns the author's name
        return self._name

    @name.setter
    def name(self, value):
        # The name can only be set ONCE (immutable)
        # If a name already exists, ignore changes
        if self._name is not None:
            return

        # Only accept a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    # Return all Article objects written by this author
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Return all Magazines this author has written for (duplicates removed)
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    # Make a new Article linked to this author
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # Return all magazine categories the author has written in
    def topic_areas(self):
        categories = {article.magazine.category for article in self.articles()}
        return list(categories) if categories else None



#   MAGAZINE CLASS

class Magazine:
    # Keep track of every magazine ever created
    all = []

    def __init__(self, name, category):
        # Use internal values so validation runs through setters
        self._name = None
        self._category = None

        # Validate name and category through setters
        self.name = name
        self.category = category

        # Add this instance to the class-level list
        Magazine.all.append(self)


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Name must be a string between 2 and 16 characters
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # Category must be a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    # Return all Article objects associated with this magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Return all unique authors who wrote for this magazine
    def contributors(self):
        return list({article.author for article in self.articles()})

    # Return a list of article titles, or None if no articles exist
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    # Return authors who wrote more than 2 articles for this magazine
    def contributing_authors(self):
        result = []

        for author in self.contributors():
            # Count how many articles this author wrote in THIS magazine
            count = len([a for a in self.articles() if a.author == author])

            if count > 2:
                result.append(author)

        return result if result else None



#   ARTICLE CLASS

class Article:
    # Track all articles created
    all = []

    def __init__(self, author, magazine, title):
        # Use internal attributes so validation happens in setters
        self._title = None
        self._author = None
        self._magazine = None

        # Validate all through setters
        self.title = title
        self.author = author
        self.magazine = magazine

        # Add article to global list
        Article.all.append(self)

    # ---- TITLE PROPERTY ----

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Title can ONLY be set once (immutable)
        if self._title is not None:
            return

        # Title must be a string between 5 and 50 characters
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value

    # ---- AUTHOR PROPERTY ----

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        # Author must be an Author instance
        if isinstance(value, Author):
            self._author = value

    # ---- MAGAZINE PROPERTY ----

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Magazine must be a Magazine instance
        if isinstance(value, Magazine):
            self._magazine = value
