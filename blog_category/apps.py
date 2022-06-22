from django.apps import AppConfig


class BlogCategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_category'
    verbose_name = 'Categories Blog'