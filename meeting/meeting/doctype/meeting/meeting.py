# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
import datetime

class Meeting(Document):
	def validate(self):
		print"\n\n validate ====="
		found = []
		for attendee in self.attendee:
			print "\n\n attendee ======",attendee
			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee.attendees)
				print "\n\n\nattendee.full_name ====",attendee.full_name

			
			print found,"found....\n\n"	
			if attendee.attendees in found:
				frappe.throw(_("Attendee {0} entered twice").format(attendee.attendees))

			
			found.append(attendee.attendees)


@frappe.whitelist()
def get_full_name(attendee):
	print "************************",attendee
	user = frappe.get_doc("User", attendee)
	print "$$$$$$$$$$$$$$",type(user),user,user.__dict__
	# return "ping"
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))



@frappe.whitelist()
def send_invitations_emails(meeting):
	print "______________________________"
	meeting = frappe.get_doc("Meeting", meeting)
	print meeting.__dict__,type(meeting.status),"hiiii\n \n "
	if meeting.get('status') == "Planned":
		print "@@@@@@@@@@@@@@@@@"
		print "planned \n\n\n"
		frappe.sendmail(recipients='sandeep.s@indictranstech.com', subject='test message for threading',
			message='testing')

		meeting.status = "Invitation Sent"
		meeting.save()
		frappe.msgprint(_("Invitation Sent"))

	else:
		frappe.msgprint(_("Meeting Status must be 'Planned'"))


@frappe.whitelist()
def get_meetings(start, end):
	if not frappe.has_permission("Meeting","read"):
		raise frappe.PermissionError

	return frappe.db.sql("""select 
		timestamp(`date`, from_time) as start,
		timestamp(`date`, to_time) as end,
		name,
		title,
		status,
		0 as all_day
	from `tabMeeting`
	where `date` between %(start)s and %(end)s""", {
		"start": start,
		"end": end		
		}, as_dict=True,debug=1)