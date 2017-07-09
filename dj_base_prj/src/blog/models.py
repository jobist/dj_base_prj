from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True)
    slug = models.SlugField(max_length=128)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'


class Article(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True)
    slug = models.SlugField(max_length=128)
    published = models.BooleanField(default=True, db_index=True, verbose_name="Published")
    short_text = models.TextField()
    full_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='Publication date')
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = 'article'

    def __str__(self):
        return self.name
