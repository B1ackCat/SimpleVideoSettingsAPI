from django.db import models
class Comment(models.Model):
    name = models.CharField(db_column='NAME', max_length=30)
    content = models.TextField(db_column='CONTENTS', max_length=1000)
    likes = models.IntegerField(db_column='NUMBER_OF_LIKES')
    hates = models.IntegerField(db_column='NUMBER_OF_HATES')
    is_author_liked = models.BooleanField(db_column="AUTHOR_LIKE")
    created_at = models.DateField(db_column='CREATED_AT', auto_now_add=True)
    updated_at = models.DateField(db_column='UPDATED_AT', auto_now=True)

    class Meta:
        managed = False
        db_table = 'comment_list'

class VideoMain(models.Model):
    title = models.CharField(db_column='TITLE', max_length=200)
    author = models.CharField(db_column='AUTHOR', max_length=30)
    views = models.IntegerField(db_column='VIEWS)
    uploaded_at = models.DateField(db_column='UPLOADED_AT', auto_now_add=True)
    description = models.TextField(db_column='DESCRIPTIONS', max_length=1000)
    playlist = models.IntegerField(db_column='PLAYLIST')
    whether_to_disclose = models.BooleanField(db_column='WHETHER_TO_DISCLOSE')
    viewer_age = models.BooleanField(db_column='VIEWER_AGE')
    age_limit = models.BooleanField(db_column='AGE_LIMIT')

    class Meta:
        managed = False
        db_table = 'video_upload'
