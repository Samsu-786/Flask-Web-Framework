from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)   # encoding it
            frame=buffer.tobytes()

        yield(b'--frame\r\n'                                                    # used yield here since it will be generating things continuously, not only one output to use return
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')           # need to give content type whenever we are doing cv.


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame') # Mimetype is also important in this place, but not sure of the reason

if __name__=="__main__":
    app.run(debug=True)

