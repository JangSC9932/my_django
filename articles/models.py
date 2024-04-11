from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'id : {self.id} | title : {self.title} | content : {self.content} | created_at: {self.created_at} '
                f'| updated_at: {self.updated_at}')