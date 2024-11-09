## Setup Instructions


### Prerequisites
Make sure you have django installed on your system.


### 1. Clone the Repository

First, clone the repository from GitHub:

```bash
git clone https://github.com/kirnath/lti_backend.git
cd lti_backend/odoo_api
python manage.py runserver
```

## 1. Endpoint: Update Leave State

**URL:** `/leaves/<leave_id>/update_state/`

**Method:** `PUT`

**Description:**  
This endpoint is used to update the state of a specific leave request based on the provided `leave_id`. The state of the leave is changed according to the value provided in the request body.

### Request Parameters:

- **`state`** (required)  
  - **Type:** string  
  - **Description:** The new state of the leave. Possible values can be something like "approved", "rejected", etc.
  
### Request Example:

```bash
curl -X PUT http://127.0.0.1:8000/leaves/42/update_state/ -d "state=approved" -H "Content-Type: application/x-www-form-urlencoded"
```

### Response:

- **Status Code:** `200 OK` (Success) or `400 Bad Request` (Error)
- **Success Response:**
  - **Content:** A JSON object indicating the success of the operation.
  - **Example:**
    ```json
    {
      "status": "success",
      "message": "Leave state updated successfully"
    }
    ```

- **Error Response:**
  - **Content:** A JSON object containing an error message.
  - **Example:**
    ```json
    {
      "status": "error",
      "message": "State parameter is required"
    }
    ```

---

## 2. Endpoint: Create Leave Request

**URL:** `/leaves/create/`

**Method:** `POST`

**Description:**  
This endpoint allows a user to create a new leave request by providing the necessary details such as employee ID, leave type, start date, end date, and reason.

### Request Parameters:

- **`employee_id`** (required)  
  - **Type:** integer  
  - **Description:** The ID of the employee requesting the leave.
  
- **`leave_type`** (required)  
  - **Type:** string  
  - **Description:** The type of leave (e.g., "sick", "vacation", etc.).
  
- **`start_date`** (required)  
  - **Type:** string (Date in `YYYY-MM-DD` format)  
  - **Description:** The start date of the leave.
  
- **`end_date`** (required)  
  - **Type:** string (Date in `YYYY-MM-DD` format)  
  - **Description:** The end date of the leave.
  
- **`reason`** (required)  
  - **Type:** string  
  - **Description:** The reason for the leave.

### Request Example:

```bash
curl -X POST http://127.0.0.1:8000/leaves/create/ -d "employee_id=123" -d "leave_type=sick" -d "start_date=2024-11-10" -d "end_date=2024-11-12" -d "reason=Feeling unwell" -H "Content-Type: application/x-www-form-urlencoded"
```

### Response:

- **Status Code:** `201 Created` (Success) or `400 Bad Request` (Error)
- **Success Response:**
  - **Content:** A JSON object containing the success status and the newly created leave's ID.
  - **Example:**
    ```json
    {
      "status": "success",
      "leave_id": 42
    }
    ```

- **Error Response:**
  - **Content:** A JSON object containing an error message.
  - **Example:**
    ```json
    {
      "status": "error",
      "message": "Invalid data"
    }
    ```

---

## General Notes:

- Both endpoints are **CSRF exempt**, meaning they bypass CSRF protection (typically useful for APIs where CSRF tokens are not feasible).
- The `Content-Type` for both requests should be `application/x-www-form-urlencoded` as they use URL-encoded data in the request body.
