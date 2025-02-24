from flask import Flask, request, jsonify, send_file
import os
import uuid

UPLOADED_IMAGES = 'uploads'
PORT = 1234

app = Flask(__name__)
os.makedirs(UPLOADED_IMAGES, exist_ok=True)

image_store = {}

@app.route('/upload', methods=['POST'])
def upload_image():
    print(":: Received image upload request")
    if 'image' not in request.files:
        print("!! Error: No image provided")
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    if image.filename == '':
        print("!! Error: Empty filename")
        return jsonify({'error': 'Empty filename'}), 400
    
    image_id = str(uuid.uuid1())
    image_path = os.path.join(UPLOADED_IMAGES, image_id + '.png')
    
    try:
        image.save(image_path)
        image_store[image_id] = image_path
        print(f":: Image saved successfully with ID {image_id}")
        return jsonify({'image_id': image_id}), 201
    except Exception as e:
        print(f"!! Error saving image: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/image/<image_id>', methods=['GET'])
def get_image(image_id):
    print(f":: Received request to fetch image ID {image_id}")
    image_path = image_store.get(image_id)
    if not image_path or not os.path.exists(image_path):
        print("!! Error: Image not found")
        return jsonify({'error': 'Image not found'}), 404
    
    print(f":: Image {image_id} retrieved successfully")
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    print(f":: Starting Flask Image Service on port {PORT}")
    app.run(debug=True, host='0.0.0.0', port=PORT)
