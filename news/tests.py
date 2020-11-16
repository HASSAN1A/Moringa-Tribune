from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt
# Create your tests here.


class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.hassan = Editor(first_name='hassan',
                             last_name='juma', email='hassanjumadev@gmail.com')
        

    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.hassan, Editor))


class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.hassan = Editor(first_name='hassan',
                             last_name='juma', email='hassanjumadev@gmail.com')
        self.hassan.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(
            title='Test Article', post='This is a random test Post', editor=self.hassan)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)
    def test_get_news_by_date(self):
        test_date = '2020-11-09'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

