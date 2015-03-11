from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Poll(models.Model):
  question = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def boolean_test(self):
    return True
  boolean_test.boolean = False

  def __unicode__(self):
    return self.question

  def was_published_recently(self):
    now = timezone.now()
    minimum_date = now - datetime.timedelta(days=1)
    return minimum_date <= self.pub_date <= now
    # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

  was_published_recently.admin_order_field = 'pub_date'
  was_published_recently.boolean = True
  was_published_recently.short_description = 'Just published?'


class Choice(models.Model):
  poll = models.ForeignKey(Poll)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __unicode__(self):
    return self.choice_text
