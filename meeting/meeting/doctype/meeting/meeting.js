// Copyright (c) 2017, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Meeting",{
	send_emails: function(frm){
		if(frm.doc.status === "Planned"){
			frappe.call({
				method: "meeting.meeting.doctype.meeting.meeting.send_invitations_emails",
				args: {
					"meeting": frm.doc.name
				},
				
			});
		}
	},

/*	to_time: function(frm){
		console.log("frm ========",frm)
		console.log("frm ====from====",frm.doc.from_time)
		console.log("frm ====to====",frm.doc.to_time)

		var fro = frm.doc.from_time;
		var to = frm.doc.to_time;
		if(fro == to){
			frappe.throw(("from_time and to_time cannot be the same"));
		}

		else if(fro > to){
			frappe.throw(("from_time cannot be less than to_time"));
		}

		else{

		}		

	},*/


});

frappe.ui.form.on('Meeting Attendee',"attendees",  function(doc,cdt, cdn) {
	var d = locals[cdt][cdn];
	console.log("jai hind",d)
	if(d.attendees){
		frappe.call({
				method:"meeting.meeting.doctype.meeting.meeting.get_full_name",
				args: {
					"attendee": d.attendees
				},
				callback: function(r) {
					if(r.message){
					d.full_name = r.message
					console.log(r.message)
					// if(r.message) {
					// 	console.log("$$$$".r.message)
					// }
				}
				}
			})
	}
});

frappe.ui.form.on("Meeting",{
	to_time: function(frm){
	var from = frm.doc.from_time;
	var to = frm.doc.to_time;
	if(from == to){
		frappe.throw(("from_time and to_time cannot be the same"));
	}

	else if(from > to){
		frappe.throw(("from_time cannot be less than to_time"));
	}

}

});
