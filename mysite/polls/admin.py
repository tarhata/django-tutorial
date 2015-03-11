from django.contrib import admin
from polls.models import Poll, Choice

class ChoicesInline(admin.TabularInline):
  model = Choice
  extra = 8

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Poll fields', {'fields': ['question']}),
    ('Date Information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoicesInline]
  list_display = ('question', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']
  search_fields = ['question']
  date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
