import os
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, jsonify, url_for, redirect
from werkzeug.utils import secure_filename
from collections import Counter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def extract_colors(image_path, num_colors=5):
    """Extract dominant colors from an image using a simple color quantization approach"""
    # Open image and convert to RGB
    image = Image.open(image_path).convert('RGB')
    
    # Resize image to speed up processing
    image = image.resize((100, 100))
    
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Reshape the array to a list of pixels
    pixels = image_array.reshape(-1, 3)
    
    # Simplify colors by rounding to nearest 20 to reduce unique colors
    simplified_pixels = (pixels // 20) * 20
    
    # Convert pixels to tuples for counting
    pixel_tuples = [tuple(pixel) for pixel in simplified_pixels]
    
    # Count occurrences of each color
    color_counts = Counter(pixel_tuples)
    
    # Get most common colors
    most_common_colors = color_counts.most_common(num_colors)
    
    # Convert to hex values and calculate percentages
    total_pixels = len(pixel_tuples)
    color_data = []
    
    for color, count in most_common_colors:
        r, g, b = color
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        percentage = (count / total_pixels) * 100
        color_data.append((hex_color, percentage))
    
    return color_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Get number of colors from form, default to 5
        num_colors = int(request.form.get('num_colors', 5))
        
        # Extract colors
        colors = extract_colors(file_path, num_colors)
        
        return render_template('result.html', 
                              filename=filename, 
                              colors=colors,
                              image_url=url_for('static', filename=f'uploads/{filename}'))
    
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True) 