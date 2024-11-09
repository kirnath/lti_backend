from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .odoo_connector import OdooConnector
import urllib.parse
@require_http_methods(["GET"])
def get_leaves(request):
    odoo = OdooConnector()
    leaves = odoo.get_leaves()
    return JsonResponse(leaves, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def create_leave(request):
    try:
        data = request.POST
        employee_id = int(data.get('employee_id'))
        leave_type = data.get('leave_type')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        reason = data.get('reason')
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    odoo = OdooConnector()
    leave_id = odoo.create_leave(employee_id, leave_type, start_date, end_date, reason)
    return JsonResponse({'status': 'success', 'leave_id': leave_id}, status=201)

@csrf_exempt
@require_http_methods(["PUT"])
def update_leave_state(request, leave_id):
    try:
        data = urllib.parse.parse_qs(request.body.decode('utf-8'))
        new_state = data.get('state', [None])[0]
        
        if not new_state:
            return JsonResponse({'status': 'error', 'message': 'State parameter is required'}, status=400)
        
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    odoo = OdooConnector()
    result = odoo.update_leave_state(leave_id, new_state)
    return JsonResponse(result)
