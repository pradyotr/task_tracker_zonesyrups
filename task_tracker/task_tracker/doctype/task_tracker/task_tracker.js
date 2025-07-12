// Copyright (c) 2025, pradyotr and contributors
// For license information, please see license.txt

frappe.ui.form.on("Task Tracker", {
    refresh(frm) {
        let d = new frappe.ui.Dialog({
            title: 'Enter Revised Due Date',
            fields: [
                {
                    label: 'Revised Due Date',
                    fieldname: 'revised_due_date',
                    fieldtype: 'Date',
                    reqd: 1,
                    minDate: frm.doc.revised_due_date

                }
            ],
            size: 'small',
            primary_action_label: 'Confirm',
            primary_action(values) {
                if (values.revised_due_date <= frm.doc.original_due_date) {
                    frappe.throw(__("Revised Due Date must be greater than Original Due Date."))
                } else if (frm.doc.revised_due_date && values.revised_due_date <= frm.doc.revised_due_date) {
                    frappe.throw(__("Revised Due Date must be greater than Current Due Date."))
                } else {
                    frm.set_value('revised_due_date', values.revised_due_date);
                    frm.set_value('extension_count', Number(frm.doc.extension_count) + 1);
                    frm.save();
                }
                d.hide();
            }
        });

        frm.add_custom_button("Extend Due Date", () => {
            d.show();
        })
    },
});
