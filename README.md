# Color Palette Extractor

A web application that extracts the most dominant colors from uploaded images. Built with Flask, Python, and Bootstrap.

## Features

- Upload images to extract color palettes
- Drag and drop interface for easy upload
- Adjustable number of colors to extract (1-10)
- Display dominant colors with their hex codes and percentages
- Copy color codes to clipboard with a single click
- Export color palettes as CSS variables or JSON
- Modern, responsive design

## Technologies Used

- **Backend**: Python, Flask
- **Image Processing**: Pillow (PIL), NumPy
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Icons**: Font Awesome

## Installation

1. Clone this repository
2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   # OR
   source venv/bin/activate  # Mac/Linux
   ```

3. Install the required packages individually:
   ```
   pip install Flask==2.0.1
   pip install Pillow==9.5.0
   pip install numpy==1.24.3
   pip install Werkzeug==2.0.2
   pip install Jinja2==3.0.3
   pip install MarkupSafe==2.0.1
   pip install itsdangerous==2.0.1
   pip install click==8.0.4
   ```

   Or install all at once:
   ```
   pip install -r requirements.txt
   ```

4. Make sure the `static/uploads` directory exists (create it if not):
   ```
   mkdir -p static/uploads
   ```

## Running the Application

1. Make sure you're in the project directory
2. Activate your virtual environment if not already active
3. Run the Flask application:
   ```
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000/`

## How It Works

The application uses a simple color quantization approach to identify the most dominant colors in an uploaded image:

1. The uploaded image is processed using the PIL library
2. Colors are simplified by rounding RGB values
3. The application counts occurrences of each color
4. The most common colors are extracted and converted to hex codes
5. The percentage of each color in the image is calculated

## License

MIT 