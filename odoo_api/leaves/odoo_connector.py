import xmlrpc.client
from django.conf import settings
from datetime import datetime

class OdooConnector:
    def __init__(self):
        self.url = settings.ODOO_URL
        self.db = settings.ODOO_DB
        self.username = settings.ODOO_USER
        self.password = settings.ODOO_PASSWORD
        
        self.common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")
        
        self.uid = self.common.authenticate(self.db, self.username, self.password, {})
        
    def get_leaves(self):
        """Retrieve all leave records from the 'leave.management' model."""
        leave_model = 'leave.management'
        leave_fields = ['id', 'employee_id', 'leave_type', 'start_date', 'end_date', 'state', 'reason']
        leaves = self.models.execute_kw(
            self.db, self.uid, self.password,
            leave_model, 'search_read',
            [[]],
            {'fields': leave_fields}
        )
        
        return leaves

    def create_leave(self, employee_id, leave_type, start_date, end_date, reason):
        """Create a new leave record in the 'leave.management' model."""
        leave_model = 'leave.management'
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
        leave_data = {
            'employee_id': employee_id,
            'leave_type': leave_type,
            'start_date': start_date,
            'end_date': end_date,
            'reason': reason,
        }
        leave_id = self.models.execute_kw(
            self.db, self.uid, self.password,
            leave_model, 'create', [leave_data]
        )
        return leave_id

    def update_leave_state(self, leave_id, new_state):
        leave_model = 'leave.management'
        valid_states = ['pending', 'approved', 'rejected']
        if new_state not in valid_states:
            return {'status': 'error', 'message': 'Invalid status value'}
        result = self.models.execute_kw(
            self.db, self.uid, self.password,
            leave_model, 'write', [[leave_id], {'state': new_state}]
        )
        
        if result:
            return {'status': 'success', 'message': f"Leave status updated to {new_state}"}
        else:
            return {'status': 'error', 'message': 'Leave record not found'}
