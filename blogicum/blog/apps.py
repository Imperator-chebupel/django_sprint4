from django.apps import AppConfig



#Не понял, зачем это, но без него не работает
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Блог'
