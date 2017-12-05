from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

# @frappe.whitelist()
# def send_invitations_emails(meeting):

# 	meeting = frappe.get_doc("Meeting", meeting)
# 	print meeting.__dict__,type(meeting.status),"hiiii\n \n "
	# meeting.check_permission("email")

	# if meeting.status = "Planned":
	# 	print "planned \n\n\n"
		# frappe.sendmail(
		# 	recipients = [d.attendee for d in meeting.attendee],
		# 	sender = frappe.seesion.user,
		# 	subject = meeting.title,
		# 	message =meeting.invitation_message,
		# 	reference_doctype = meeting.doctype,
		# 	reference_name = meeting.name,
		# 	as_bulk = True
		# 	)

	# 	meeting.status = "Invitation Sent"
	# 	meeting.save()
	# 	meetint.msgprint(_("Invitation Sent"))

	# else:
	# 	frappe.msgprint(_("Meeting Status must be 'Planned'"))