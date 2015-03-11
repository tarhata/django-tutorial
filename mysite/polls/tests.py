"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from polls.models import Poll

def create_Poll(question, days):
  """
  Creates a poll with the given `question` published the given number of
  days offset to now (negative for polls published in the past,
  positive for polls that have yet to be published).
  """
  return Poll.objects.create(question=question, pub_date=timezone.now() + datetime.timedelta(days=days))

class PollViewTests(TestCase):
  def test_index_view_with_no_polls(self):
    """
    If no poll exists, a message is displayed
    """
    response = self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200) # checks that page loaded
    self.assertContains(response, "No polls are available.") # asserts message
    self.assertQuerysetEqual(response.context['latest_poll_list'], []) # checks if latest_poll_list empty

  def test_index_view_with_a_past_poll(self):
    """
    Polls with

class PollMethodTests(TestCase):
  def test_was_published_recently_with_future_poll(self):
    future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=1))
    self.assertEqual(future_poll.was_published_recently(), False)

  def test_was_published_recently_with_old_poll(self):
    """ was_published_recently() should return FALSE for polls whose pub_date is older than one days """
    old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
    self.assertEqual(old_poll.was_published_recently(), False)

  def test_was_published_recently_with_recent_poll(self):
    """ was_published_recently() should return TRUE for polls whose pub_date is within the last days """
    recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
    self.assertEqual(recent_poll.was_published_recently(), True)

# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)
