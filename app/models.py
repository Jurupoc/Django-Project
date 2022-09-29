from django.db import models

DESCRIPTION_MAX_LENGTH = 300
TITLE_MAX_LENGTH = 20


class Topic(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=20)

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)

    created_at = models.DateTimeField(auto_now_add=True)
    # TODO: Create a author Field.


class Post(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=20)

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: Create a author Field.


class Comment(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: Create a author Field.
