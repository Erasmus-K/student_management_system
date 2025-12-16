from flask import Flask, render_template, request, redirect
from models import get_connection, init_db
from datetime import date

app = Flask(__name__)
init_db()

# Home Page
@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Get stats for dashboard
    cursor.execute("SELECT COUNT(*) FROM FeeStructure")
    fee_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM Attendance")
    attendance_count = cursor.fetchone()[0]
    
    conn.close()
    
    return render_template("index.html", fee_count=fee_count, attendance_count=attendance_count)

# Finance Module
@app.route("/add-fee", methods=["GET", "POST"])
def add_fee():
    if request.method == "POST":
        course = request.form["course"]
        amount = request.form["amount"]
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO FeeStructure(course, amount) VALUES(?,?)",
                       (course, amount))
        conn.commit()
        conn.close()
        return redirect("/add-fee")
    return render_template("add_fee.html")

@app.route("/view-fees")
def view_fees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM FeeStructure")
    fees = cursor.fetchall()
    conn.close()
    return render_template("finance.html", fees=fees)

# Attendance Module
@app.route("/record-attendance", methods=["GET", "POST"])
def record_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    
    if request.method == "POST":
        student_id = request.form["student_id"]
        course = request.form["course"]
        status = request.form["status"]
        
        cursor.execute(
            "INSERT INTO Attendance(student_id, course, date, status) VALUES(?,?,?,?)",
            (student_id, course, date.today(), status)
        )
        conn.commit()
        conn.close()
        return redirect("/record-attendance")
    
    # Get available courses from FeeStructure
    cursor.execute("SELECT DISTINCT course FROM FeeStructure ORDER BY course")
    courses = cursor.fetchall()
    
    # Get all students
    cursor.execute("SELECT id, name, course FROM Students ORDER BY name")
    students = cursor.fetchall()
    
    conn.close()
    
    return render_template("record_attendance.html", courses=courses, students=students)

@app.route("/view-attendance")
def view_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.id, s.name, a.course, a.date, a.status 
        FROM Attendance a 
        JOIN Students s ON a.student_id = s.id 
        ORDER BY a.date DESC, s.name
    """)
    attendance = cursor.fetchall()
    conn.close()
    return render_template("attendance.html", attendance=attendance)

# Students Module
@app.route("/students")
def students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students ORDER BY name")
    students = cursor.fetchall()
    conn.close()
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
