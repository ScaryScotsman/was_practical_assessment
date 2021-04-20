from datetime import timedelta, datetime

from django.db import models


class Article(models.Model):
    article_heading = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    article_content = models.CharField(max_length=2000)

    def __str__(self):
        return self.article_heading

    # def was_published_recently(self):
    #     return self.pub_date >= datetime.now() - timedelta(days=1)
