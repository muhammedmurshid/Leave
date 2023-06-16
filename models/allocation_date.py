from odoo import fields, models, _, api
import requests


class LeaveAllocationDate(models.Model):
    _inherit = 'hr.leave.allocation'

    date_allocation = fields.Date(string='Date', required=True)

    @api.model
    def create(self, values):
        mobile = "9567799581"
        user = "HR Manager"
        type = "Leave Allocation"
        message_approved = "Hi " + user + ", an employee has requested " + type + " in Logic HRMS. For more details login to https://corp.logiceducation.org"
        dlt_approved = '1107168689563797302'

        url = "http://sms.mithraitsolutions.com/httpapi/httpapi?token=adf60dcda3a04ec6d13f827b38349609&sender=LSMKCH&number=" + str(
            mobile) + "&route=2&type=Text&sms=" + message_approved + "&templateid=" + dlt_approved

        # A GET request to the API
        response = requests.get(url)

        # Print the response
        response_json = response.json()
        print(response_json)
        return super(LeaveAllocationDate, self).create(values)

    def action_approve(self):
        emp_name = []
        emp_phone = []
        emp_phone.append(self.employee_id.work_phone)
        emp_name.append(self.employee_id.name)
        employee_name = ' '.join(emp_name)
        number = ' '.join(emp_phone)

        type = self.holiday_status_id.name + ' Allocation Request'
        status = "Approved"
        message_approved = "Hi " + employee_name + ", your " + type + " has been " + status + " in Logic HRMS. For more details login to https://corp.logiceducation.org"
        dlt_approved = '1107168689839574197'

        url = "http://sms.mithraitsolutions.com/httpapi/httpapi?token=adf60dcda3a04ec6d13f827b38349609&sender=LSMKCH&number=" + str(
            number) + "&route=2&type=Text&sms=" + message_approved + "&templateid=" + dlt_approved

        # A GET request to the API
        response = requests.get(url)

        # Print the response
        response_json = response.json()
        print(response_json)
        return super(LeaveAllocationDate, self).action_approve()

    def action_refuse(self):
        emp_name = []
        emp_phone = []
        emp_phone.append(self.employee_id.work_phone)
        emp_name.append(self.employee_id.name)
        employee_name = ' '.join(emp_name)
        number = ' '.join(emp_phone)

        type = self.holiday_status_id.name + ' Allocation Request'
        status = "Rejected"
        message_approved = "Hi " + employee_name + ", your " + type + " has been " + status + " in Logic HRMS. For more details login to https://corp.logiceducation.org"
        dlt_approved = '1107168689839574197'

        url = "http://sms.mithraitsolutions.com/httpapi/httpapi?token=adf60dcda3a04ec6d13f827b38349609&sender=LSMKCH&number=" + str(
            number) + "&route=2&type=Text&sms=" + message_approved + "&templateid=" + dlt_approved

        # A GET request to the API
        response = requests.get(url)

        # Print the response
        response_json = response.json()
        print(response_json)
        return super(LeaveAllocationDate, self).action_refuse()
