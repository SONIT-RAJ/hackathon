from flask import Flask, render_template, Response
from opencv2 import gen_frames  # Import the video stream generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patient_monitoring')
def patient_monitoring():
    # Render the template that displays the live video feed
    return render_template('facedet.html')

@app.route('/video_feed')
def video_feed():
    # Return the video streaming response using the generator function
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
