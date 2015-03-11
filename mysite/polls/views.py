from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Poll, Choice

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_poll_list'

  def get_queryset(self):
    # """Return the last n published polls."""
    # return Poll.objects.order_by('-pub_date')[:10]
    """Return the last n published polls that aren't set in the future
       pub_date__lte returns a queryset of Polls whose pub_date is less than
       or equal to timeszone.now """
    return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
  model = Poll
  template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  model = Poll
  template_name = 'polls/results.html'

def vote(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  try:
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the poll voting form.
    return render(request, 'polls/detail.html', {
                  'poll': p,
                  'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    """
    Always return an HttpReponseRedirect after succesfully dealing with POST data.
    Prevents data from being posted twice if a user hits the back button
    """
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
