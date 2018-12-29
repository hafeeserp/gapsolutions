frappe.ui.form.on('Salary Slip', {
	from_date:function(frm){
		current_date = new Date()
	
		current_date = moment(current_date)
	
		from_date=moment(frm.doc.from_date)
	
		var days = current_date.diff(from_date, 'days')
	
		frm.set_value("arrear_days",days)
	},
	increment_percentage:function(frm){
		if(frm.doc.increment_percentage){
			frm.set_value("increment_amount",(frm.doc.gross_pay*frm.doc.increment_percentage)/100*frm.doc.arrear_days)
			frm.set_value("total_arrears",frm.doc.gross_pay+frm.doc.increment_amount)
			frm.set_value("net_pay_with_arrears",frm.doc.net_pay+frm.doc.increment_amount)
		}
	},
  	arrear_days:function(frm){
		frm.set_value("increment_amount",(frm.doc.gross_pay*frm.doc.increment_percentage)/100*frm.doc.arrear_days)
                frm.set_value("total_arrears",frm.doc.gross_pay+frm.doc.increment_amount)
		frm.set_value("net_pay_with_arrears",frm.doc.net_pay+frm.doc.increment_amount)
	},
	employee:function(frm){
		frappe.call({
      			"method": "frappe.client.get_value",
      			"args": {
         			"doctype": "Department",
         			"filters": frm.doc.department,
			        "fieldname": "increment_percentage"
       			},
      			"callback": function(res){
        		          cur_frm.set_value("increment_percentage", res.message.increment_percentage);
        		}
      		
    		});
		get_emp_and_leave_details(frm.doc, dt, dn);
	}
	

});
var calculate_net_pay = function(doc, dt, dn) {
	doc.net_pay = flt(doc.gross_pay) - flt(doc.total_deduction);
	doc.rounded_total = Math.round(doc.net_pay);

	doc.total_fixed = flt(doc.fixed) - flt(doc.fixed_duduction);
	doc.total_variant = flt(doc.variant) - flt(doc.variant_deduction);
	if(doc.arrear_days){
		doc.increment_amount = (doc.gross_pay*doc.increment_percentage)/100*doc.arrear_days
        	doc.total_arrears = doc.gross_pay+doc.increment_amount
		doc.net_pay_with_arrears = doc.net_pay + doc.increment_amount
	}
	refresh_many(['net_pay', 'rounded_total','total_variant','total_fixed','increment_amount','total_arrears','net_pay_with_arrears']);
}
	

