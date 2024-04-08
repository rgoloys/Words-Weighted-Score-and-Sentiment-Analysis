To run the code type "python manage.py runserver" in terminal, but make sure to locate the directory of your file.


The following package are required to install:

pip install django => neccesary to use django framework
pip install python-docx => used to read document file
pip install PyPDF2 => used to read pdf file
pip install openpyxl => used to read excel file
pip install textblob => algorithm used for sentiment analysis
pip install nltk => Natural Language Toolkit used for text tokenizing for the word score function
pip install django-allauth => for google auth built in feautures

To access database by using sqlite3 run:
 python manage.py makemigrations
 python manage.py migrate

To Create a admin accounts:
 python manage.py createsuperuser

ALGORITHM USED FOR SENTIMENT ANALYSIS ARE THE "TextBlob"


TextBlob is a Python library for processing textual data. It provides a simple API for common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

TextBlob is built on top of NLTK (Natural Language Toolkit) and also uses pattern libraries. It offers a more simplified interface compared to NLTK, making it easier for beginners to work with. TextBlob provides a consistent API and handles the complexities of text processing tasks under the hood, allowing users to focus on their specific NLP applications without worrying about the implementation details.

Some common use cases of TextBlob include sentiment analysis of social media data, extracting key phrases from text, and classifying text into categories. Overall, TextBlob is a convenient tool for text processing and analysis in Python.



TO DO:

highlights in docs file