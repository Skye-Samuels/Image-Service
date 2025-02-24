import requests
import os

PORT = "1234"
BASE_URL = f"http://127.0.0.1:{PORT}"
IMAGES_FOLDER = "test images"

def upload_image(image_path):
    if not os.path.exists(image_path):
        print(f"! Error: File {image_path} does not exist.")
        return {"error": "File does not exist"}
    
    print(f"+ Uploading: {image_path.ljust(20)}")
    with open(image_path, "rb") as img:
        files = {"image": img}
        response = requests.post(f"{BASE_URL}/upload", files=files)
    result = response.json()
    if "image_id" in result:
        print(f": Response: {result['image_id']}")
    else:
        print(f"! Error: {result}")
    return result

def get_image(image_id, output_path):
    print(f"+ Fetching Image ID: {image_id}")
    response = requests.get(f"{BASE_URL}/image/{image_id}", stream=True)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f": Image saved as: {output_path.ljust(16)}")
    else:
        print(f"! Error: {response.json()} ")

if __name__ == "__main__":
    print("+********************************+")
    print("*   Image Upload and Retrieval   *")
    print("+********************************+\n")
    
    input("* Press Enter to upload cat.jpg...")
    print("\n")
    cat_path = os.path.join(IMAGES_FOLDER, "cat.jpg")
    response = upload_image(cat_path)
    if "image_id" in response:
        cat_id = response["image_id"]
        input("* Press Enter to fetch cat.jpg...")
        print("\n")
        get_image(cat_id, "downloaded_cat.jpg")
    
    input("* Press Enter to upload dog.png...")
    print("\n")
    dog_path = os.path.join(IMAGES_FOLDER, "dog.png")
    response = upload_image(dog_path)
    if "image_id" in response:
        dog_id = response["image_id"]
        input("* Press Enter to fetch dog.png...")
        print("\n")
        get_image(dog_id, "downloaded_dog.png")
    
    input("* Press Enter to attempt invalid upload...")
    print("\n")
    invalid_path = os.path.join(IMAGES_FOLDER, "non_existent.jpg")
    upload_image(invalid_path)
    
    input("* Press Enter to attempt invalid download...")
    print("\n")
    invalid_image_id = "invalid_id_1234"
    get_image(invalid_image_id, "invalid_download.jpg")
