from django.shortcuts import render
from .models import IssueTicket
from django.contrib.auth.decorators import login_required

# Create your views here.


def index_route(request):
	""" This is the default page a user lands on when they visit the website.
	"""
	return render(request, "userticketing/index.html")

def about_route(request):
	"""
	This function renders a html page for the about route.
	"""
	return render(request, "userticketing/about.html")


def blog_route(request):
	"""
	This function renders available blogs on the blogs page.
	"""
	return render(request, "userticketing/blogs.html")

def contact_route(request):
	"""
	This function renders the html page for the contact route.
	"""
	return render(request, "userticketing/contact.html")


@login_required(login_url="login")
def dashboard_route(request):
	"""
	This is the route a user is redirected to on successful login.
	"""
	# retrieve current user accessing the dashboard
	user_name = request.user

	# get available tickets by that user
	user_tickets = IssueTicket.objects.filter(issue_creator=user_name)

	# get tickets by each type
	pending_tickets = len(IssueTicket.objects.filter(issue_creator=user_name, issue_status="Pending").values())
	resolved_tickets = len(IssueTicket.objects.filter(issue_creator=user_name, issue_status="Resolved").values())
	total_tickets = pending_tickets + resolved_tickets

	return render(request, "userticketing/dashboard.html", {"title": "iTicket", "current_tickets": user_tickets, "resolved_tickets": resolved_tickets, "pending_tickets": pending_tickets, "total_tickets": total_tickets})
