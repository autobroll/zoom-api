from flask import Flask, request, send_file
import subprocess
import requests

app = Flask(__name__)

@app.route('/zoom', methods=['POST'])
def zoom_effect():
    image_url = request.json['image_url']
    response = requests.get(image_url)
    with open('input.jpg', 'wb') as f:
        f.write(response.content)

    subprocess.run([
        'ffmpeg', '-y', '-loop', '1', '-i', 'input.jpg',
        '-filter_complex', "zoompan=z='zoom+0.001':d=125,scale=720:1280",
        '-t', '5', '-r', '25', 'output.mp4'
    ])

    return send_file('output.mp4', mimetype='video/mp4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
