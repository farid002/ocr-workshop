from flask import Blueprint, render_template, request, redirect, url_for, send_file, flash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload():
    pass

@main.route('/dashboard')
def dashboard():
    pass

@main.route('/download_pdf/<int:id>')
def download_pdf(id):
    pass

@main.route('/webcam')
def webcam():
    pass