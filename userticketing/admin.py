from django.contrib import admin
from .models import IssueTicket
from django.contrib.auth.models import User


# change default site labels
admin.site.site_header = "iTicket"
admin.site.site_title = "iTicket administration"
admin.site.index_title = "iTicket | Admin"



class NewUserIssue(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': [
         'issue_creator', 'issue_creator_email']}),
        ('Issue information', {'fields': [
            'issue_content', 'issue_status']}),
        ('Date information', {'fields': [
         'date_issue_created']}),
    ]

# change how to display usernotes model
class IssueTicketInline(admin.TabularInline):
    model = IssueTicket
    extra = 0


class IssueTicketInlineAdmin(admin.ModelAdmin):
    inlines = [IssueTicketInline]


# register the custom user model
# admin.site.unregister(User)
# admin.site.register(UserNotes)
admin.site.register(IssueTicket, NewUserIssue)