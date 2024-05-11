To run the code type "python manage.py runserver" in terminal, but make sure to locate the directory of your file.


The following package are required to install:

pip install django => neccesary to use django framework
pip install python-docx => used to read document file
pip install PyPDF2 => used to read pdf file
pip install openpyxl => used to read excel file
pip install textblob => libraries used for sentiment analysis
pip install nltk => Natural Language Toolkit used for text tokenizing for the word score function
pip install django-allauth => for google auth built in feautures

To access database by using sqlite3 run:
 python manage.py makemigrations
 python manage.py migrate

To Create a admin accounts:
 python manage.py createsuperuser

libraries USED FOR SENTIMENT ANALYSIS ARE THE "TNLTK's SentimentIntensityAnalyzer"

We compare 3 libraries for sentiment analysis function and we come up to used NLTK's SentimentIntensityAnalyzer.
The 3 libraries we used to compare are the TextBlob, Vader, NLTK's SentimentIntensityAnalyzer.

During the testing, we notice that TextBlob is not accurate in analyzing and providing it's score. However, the Vader libraries
has the most accurate analysis but take a lot of time analyzing. Therefore, the NLTK's SentimentIntensityAnalyzer are great in 
analyzing and at the same time provide an accurate analysis.



