# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Episodes(models.Model):
    # This field type is a guess.
    show_url = models.TextField(blank=True, null=True)
    # This field type is a guess.
    season_title = models.TextField(blank=True, null=True)
    # This field type is a guess.
    season_number = models.IntegerField(blank=True, null=True)
    # This field type is a guess.
    episode_number = models.TextField(blank=True, null=True)
    # This field type is a guess.
    episode_title = models.TextField(blank=True, null=True)
    # This field type is a guess.
    link = models.TextField(primary_key=True, blank=True, null=False)
    # This field type is a guess.
    url_title = models.TextField(blank=True, null=True)
    # This field type is a guess.
    language = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'episodes'


class Shows(models.Model):
    # This field type is a guess.
    show_id = models.TextField(primary_key = True, blank=True, null=False)
    # This field type is a guess.
    show_title = models.TextField(blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    show_picurl = models.TextField(
        db_column='show_picUrl', blank=True, null=True)
    # This field type is a guess.
    show_counts = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shows'
