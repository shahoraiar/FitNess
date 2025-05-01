# FitNess
# 👤 User App

This app manages user authentication using JWT, including registration, login, token refresh, and profile viewing.

---

## 📦 User Model

The `User` model extends Django’s `AbstractUser` and adds a `user_type` field to differentiate between `admin` and `customer` users.  
By default, all registered users are assigned the `customer` role.

---

## 🔑 API Endpoints

### 1. Register New User
**Endpoint:** `POST /api/user/register/`  
This endpoint creates a new user with the `username`, `email`, and `password`. The `user_type` is automatically set to `"customer"`.  
**Required fields:**  
- `username` (string)  
- `email` (string)  
- `password` (string, minimum 6 characters)

**Returns:** A success message if the user is created successfully, or error messages if validation fails.

---

### 2. Login (JWT Token)
**Endpoint:** `POST /api/user/login/`  
This endpoint returns a JWT access token and refresh token upon providing correct credentials.

**Required fields:**  
- `username`  
- `password`

**Returns:**  
- `access` token (used in authenticated requests)  
- `refresh` token (used to get a new access token)

---

### 3. Refresh JWT Token
**Endpoint:** `POST /api/user/token/refresh/`  
This endpoint takes a valid refresh token and returns a new access token.

**Required fields:**  
- `refresh` token

**Returns:**  
- A new `access` token

---

### 4. Get User Profile
**Endpoint:** `GET /api/user/profile/`  
This endpoint returns the profile data of the currently authenticated user.  
**Authorization:** Bearer token must be included in the headers using the access token from the login endpoint.

**Returns:**  
- User `id`  
- `username`  
- `email`  
- `user_type`

---

## ⚙️ JWT Configuration

JWT settings in `settings.py`:

- Access token lifetime: 60 minutes
- Refresh token lifetime: 7 days
- Rotation and blacklisting: Disabled
- Update last login: Disabled

```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
}
```


# 🏋️ Workout App

This app manages **workout video uploads**, **listings**, **updates**, and **deletions**.  
Only **authenticated admin users** can create or manage workouts.  
Videos are stored in **Cloudinary**.

---

## 📦 Model: `Workout`

Represents a workout video and its metadata.

### Fields:
- `title`: Title of the workout  
- `description`: Text description  
- `duration`: Duration in minutes  
- `goal`: One of `weight_loss`, `muscle_gain`, `flexibility`  
- `difficulty`: One of `beginner`, `intermediate`, `advanced`  
- `video`: Stored in Cloudinary  
- `uploaded_by`: Linked to the user who uploaded it  
- `created_at`: Timestamp (auto-filled)

---

## 🔑 API Endpoints

> All endpoints require **JWT authentication**.  
> Only users with `user_type = "admin"` are allowed.

---

### 1. 🚀 Create Workout  
**POST** `/api/workouts/`

**Request Fields (form-data)**:
- `title`
- `description`
- `duration`
- `goal`
- `difficulty`
- `video`

**Response**: Created workout object with metadata.

---

### 2. 📋 List All Workouts  
**GET** `/api/workouts/`

Returns a list of all workout objects.

---

### 3. 🔍 Get Workout Details  
**GET** `/api/workouts/<id>/`

Returns a single workout object by its ID.

---

### 4. ✏️ Update Workout  
**PUT** `/api/workouts/<id>/`

Updates workout fields.  
Only the uploader (admin) can update.

---

### 5. ❌ Delete Workout  
**DELETE** `/api/workouts/<id>/`

Deletes the workout video and metadata.

---

## 🔐 Permissions

- `IsAuthenticated`  
- `IsAdminUserType` (custom permission)

✅ Only admin users can create, update, or delete workouts.

## ⚙️ Create an Admin User

1. Run the following command to create a superuser:

```bash
python manage.py createsuperuser
python manage.py shell
from app.user.models import User  # update this import based on your project structure

user = User.objects.get(email="your-admin-email@example.com")
user.user_type = "admin"
user.save()
---
```
# 🥗 AI Meal Plan Generator

This app uses an AI API to generate personalized **daily or weekly meal plans** based on the user's physical data and fitness goals.  
Only **authenticated users** can access the generator.

---

## 📦 Endpoint

### 🔮 1. Generate AI-Powered Meal Plan  
**POST** `/api/mealplan/generate/`  
(Requires **JWT authentication**)

---

## 📥 Request Fields (JSON):
| Field                | Type      | Choices                                       | Required |
|---------------------|-----------|------------------------------------------------|----------|
| `goal`              | string    | `"weight_loss"`, `"muscle_gain"`, `"balanced"` | ✅ |
| `duration`          | string    | `"daily"`, `"weekly"`                          | ✅ |
| `age`               | integer   | (e.g. 25)                                      | ✅ |
| `weight`            | float     | (e.g. 70.5) kg                                 | ✅ |
| `height`            | float     | (e.g. 175.0) cm                                | ✅ |
| `gender`            | string    | `"male"`, `"female"`, `"other"`                | ✅ |
| `activity_level`    | string    | `"sedentary"`, `"moderate"`, `"active"`        | ✅ |
| `sleep_hours_per_night` | float | (e.g. 7.5) hours                               | ✅ |

---

## 📤 Response

On success:

```json
{
  "meal_plan": "Your custom daily or weekly meal plan with meals, calories, macros..."
}
```
## 🤖 AI Model Details

- **API**: Uses **OpenRouter.ai** API.
- **AI Model**: `deepseek/deepseek-r1:free`.
- **Prompt Includes**: 
  - Age
  - Weight
  - Height
  - Gender
  - Goal (e.g., weight loss, muscle gain, balanced)
  - Activity Level (e.g., sedentary, moderate, active)
  - Sleep Hours Per Night

---

## 🔐 Permissions

- **Authentication**: Requires `IsAuthenticated` permission.
- **Who Can Access**: 
  - Both **admin** and **customer** users can request a meal plan.
