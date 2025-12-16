# Student Management System

A modern web-based Student Management System built with Flask, featuring a beautiful dashboard interface for managing student attendance and fee structures.

## Features

- 📊 **Modern Dashboard** - Clean, responsive interface with sidebar navigation
- 💰 **Fee Management** - Add and view course fee structures
- 📅 **Attendance Tracking** - Record and view student attendance with course selection
- 👥 **Student Management** - View registered students
- 🎨 **Beautiful UI** - Modern design with gradients and smooth animations

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install Flask
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the Application**
   Open your browser and go to: `http://localhost:5000`

## Usage

### Dashboard
- Navigate through different modules using the sidebar
- View quick stats for fees and attendance records

### Fee Management
- Add new course fee structures
- View all existing fee structures

### Attendance Management
- Record attendance by selecting students and courses from dropdowns
- View all attendance records with student names and status indicators

### Student Management
- View all registered students in the system
- Students are pre-populated with sample data

## Database

The application uses SQLite database (`database.db`) which is automatically created on first run with sample data including:
- 5 sample students
- Empty fee structures (add your own)
- Empty attendance records (record as needed)

## File Structure

```
Student-Management/
├── app.py              # Main Flask application
├── models.py           # Database models and initialization
├── config.py           # Configuration file
├── requirements.txt    # Python dependencies
├── database.db         # SQLite database (auto-created)
├── static/
│   └── style.css      # Modern CSS styling
└── templates/
    ├── base.html      # Base template with sidebar
    ├── index.html     # Dashboard homepage
    ├── add_fee.html   # Add fee structure form
    ├── finance.html   # View fee structures
    ├── record_attendance.html  # Record attendance form
    ├── attendance.html         # View attendance records
    └── students.html          # View students
```

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome
- **Styling**: Custom CSS with gradients and animations