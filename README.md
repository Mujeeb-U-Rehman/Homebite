# HomeBite

🍽️ **Hyperlocal home-cooked meals marketplace** - Connecting home cooks with office workers for fresh, homemade meals.

## 🌟 Features

### For Customers (Office Workers)
- Browse nearby meals within 1-2 km radius
- View meal details including cook ratings
- Place orders with pickup or delivery options
- Track order status
- Rate completed orders
- Manage office location with map picker

### For Home Cooks
- Create and manage meal listings
- Dashboard with today's orders and stats
- Mark orders as ready/completed
- Build reputation through ratings
- Kitchen location on map

### For Admins
- Approve/reject cook accounts
- Approve/reject meal listings
- View all orders with filters
- User management (enable/disable)
- Dashboard with statistics

## 🛠️ Tech Stack

- **Backend**: Django 4.2+ with Django REST Framework
- **Frontend**: Django Templates + Bootstrap 5
- **Database**: PostgreSQL (SQLite for development)
- **Maps**: Leaflet.js + OpenStreetMap (free)
- **Deployment**: Vercel-compatible configuration
- **Static Files**: WhiteNoise

## 📋 Prerequisites

- Python 3.10+
- PostgreSQL (for production)
- pip (Python package manager)

## 🚀 Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mujeeb-U-Rehman/Homebite.git
cd Homebite
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=  # Leave empty for SQLite
```

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

Default admin credentials for testing:
- Username: `admin`
- Email: `admin@homebite.com`
- Password: `admin123`

### 7. Run the development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 to see the application.

## 📁 Project Structure

```
Homebite/
├── manage.py
├── requirements.txt
├── vercel.json                 # Vercel deployment config
├── build_files.sh              # Build script for Vercel
├── homebite/                   # Main project
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/                   # User management app
│   ├── models.py              # User, CookProfile, CustomerProfile
│   ├── views.py               # Signup, login, profile views
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/accounts/
├── meals/                      # Meals app
│   ├── models.py              # Meal model
│   ├── views.py               # CRUD, browse, search
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/meals/
├── orders/                     # Orders app
│   ├── models.py              # Order model
│   ├── views.py               # Place order, order history
│   ├── urls.py
│   ├── admin.py
│   └── templates/orders/
├── dashboard/                  # Cook dashboard app
│   ├── views.py
│   ├── urls.py
│   └── templates/dashboard/
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── media/                      # Uploaded images
├── templates/
│   ├── base.html
│   └── home.html
└── README.md
```

## 🗄️ Database Models

### User (extends AbstractUser)
- `role`: cook/customer/admin
- `phone`: contact number
- `address`: user address
- `cnic`: optional ID number
- `is_approved`: admin approval status

### CookProfile
- Kitchen location (lat/lng)
- Kitchen address
- Rating (0-5)
- Total orders/ratings

### CustomerProfile
- Office location (lat/lng)
- Office address

### Meal
- Name, description, photo
- Price (PKR)
- Quantity available
- Ready time
- Approval status

### Order
- Customer, meal, cook references
- Quantity, total price
- Status (pending/confirmed/ready/completed/cancelled)
- Delivery type (pickup/delivery)
- Payment method (cash)

## 🌐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Django secret key | Yes |
| `DEBUG` | Debug mode (True/False) | No (default: True) |
| `ALLOWED_HOSTS` | Comma-separated hosts | No |
| `DATABASE_URL` | PostgreSQL connection URL | No (SQLite fallback) |

## 🚀 Vercel Deployment

### 1. Install Vercel CLI

```bash
npm install -g vercel
```

### 2. Configure environment variables on Vercel

Set the following in your Vercel project settings:
- `SECRET_KEY`: Generate a strong secret key
- `DEBUG`: False
- `ALLOWED_HOSTS`: your-app.vercel.app
- `DATABASE_URL`: Your PostgreSQL connection string (Vercel Postgres, Supabase, or Neon)

### 3. Deploy

```bash
vercel
```

### Database Options for Vercel

1. **Vercel Postgres** (Recommended)
   - Create from Vercel dashboard
   - Connection string auto-injected

2. **Supabase**
   - Free tier available
   - Get connection string from project settings

3. **Neon**
   - Serverless PostgreSQL
   - Perfect for Vercel deployments

### Static & Media Files

- **Static files**: Served via WhiteNoise
- **Media files**: For production, use Cloudinary or AWS S3

## 📱 Pages

1. **Home Page** - Hero section, how it works, featured meals
2. **Cook Signup** - Multi-step form with location picker
3. **Customer Signup** - Simple form with office location
4. **Login** - For both roles
5. **Browse Meals** - Card grid with filters
6. **Meal Detail** - Full details, cook info, order button
7. **Place Order** - Quantity, delivery type, confirm
8. **Order Confirmation** - Success page with details
9. **Customer Order History** - List of past orders
10. **Cook Dashboard** - Today's orders, actions, stats
11. **Cook Meal Management** - Add/edit/delete meals
12. **Profile Pages** - Edit profile for both roles

## 🔧 Admin Panel

Access at `/admin/` with superuser credentials.

**Features:**
- Approve/reject cook accounts
- Approve/reject meal listings
- View all orders with status filters
- User management (enable/disable)
- Bulk actions for efficiency

## 📝 API Endpoints

The application uses Django REST Framework for API support:

- `GET /meals/` - Browse meals
- `GET /meals/<id>/` - Meal detail
- `POST /orders/place/<meal_id>/` - Place order

## 🔒 Security Features

- CSRF protection on all forms
- Secure password hashing (Django's PBKDF2)
- Role-based access control
- Session-based authentication
- Input validation on all forms

## 🧪 Testing

```bash
python manage.py test
```

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support, please open an issue on GitHub or contact the maintainers.

---

Made with ❤️ for home cooks and food lovers
