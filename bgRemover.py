from flask import Flask, request, render_template, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def upload_page():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No file selected", 400

    # Process the image
    input_image = file.read()
    output_image = remove(input_image)

    # Save the result in memory
    output = io.BytesIO(output_image)
    output.seek(0)

    # Return the processed image
    return send_file(output, mimetype='image/png', as_attachment=True, download_name='output.png')

if __name__ == '__main__':
    app.run(debug=True)
