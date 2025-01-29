from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

# Create your models here.
"""
note fields
	id uid
	note sender - char field email
	 // note recipient - list users in drop down
	note content - text
	note status - default pending
	note time auto filled time
"""

class IssueTicket(models.Model):
    # define a custom primary key for the table
    id = models.UUIDField(
        help_text="Unique Identifier for an issue",
        primary_key = True,
        default = uuid.uuid4,
        editable = False
        )

    # user creating an issue
    issue_creator = models.ForeignKey(
        to=User,
        help_text="Current logged in user creating the issue",
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    )

    # recipient of the issue
    # issue_recipient = models.ForeignKey(
    #     to=User,
    #     help_text="Current logged in user creating the issue",
    #     on_delete=models.DO_NOTHING,
    #     blank=False,
    #     null=False
    # )

    # email of user creating the issue
    issue_creator_email = models.EmailField(
        help_text="Email of current user",
        max_length=150,
        null=False
    )

    # issue data
    issue_content = models.TextField(
        help_text="Actual content of the issue being created",
        blank=False,
        null=False
    )

    # status of the issue
    issue_status = models.CharField(
        verbose_name = "Status of issue",
        help_text="Current status of issue",
        choices=[
            ("Pending", "Pending"),
            ("Resolved", "Resolved"),
            ("Cancelled", "Cancelled")
        ],
        max_length=15,
        null=False
    )

    # time the issue was created
    date_issue_created = models.DateTimeField(
        help_text="Time issue was created",
        default=timezone.now,
        null=False
    )


    def __str__(self):
        return f"{self.issue_creator} registered an issue"

    class Meta:
        verbose_name_plural = "Tickets"
        ordering = ["-date_issue_created"]