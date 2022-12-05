from app import app 
from flask import render_template

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route("/admin/admin_profile")
def admin_profile():
    return "<h1>Abdmin profile :(1)(11)(1(111111)11 </h1>"