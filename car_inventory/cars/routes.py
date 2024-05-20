from flask import Blueprint, render_template

cars_bp = Blueprint('cars', __name__)

@cars_bp.route('/inventory')
def inventory():
    return render_template('inventory.html')
