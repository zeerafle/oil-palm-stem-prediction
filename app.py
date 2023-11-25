import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from utils import predict

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def predict_image_file():
    if request.method == 'POST':
        f = request.files
        if 'file' not in f:
            return 'No file part', 400
        uploaded_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f['file'].filename))
        f['file'].save(uploaded_path)
        prediction = predict(uploaded_path)
        return render_template('index.html', prediction=prediction, image_path=uploaded_path)


if __name__ == '__main__':
    app.run()
