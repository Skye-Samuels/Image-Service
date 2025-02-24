# Flask Image Service

## Overview
This microservice allows users to upload and retrieve images via a very simple REST API. Uploaded images receive a unique UUID, which can be used to retrieve them them later.

## Communication Contract

1. **Upload an Image**
- **Endpoint**: POST /upload
- **Description**: Upload an image file and receive a unique image_id.
- **Request Format**:
  - Form-data: image (file)
- **Response Format**:
  - JSON: { "image_id": "<unique_image_id>" }
- **Example Request**:

```py
    import requests
    
    url = "http://127.0.0.1:1234/upload"
    files = {"image": open("cat.jpg", "rb")}
    response = requests.post(url, files=files)
    print(response.json())  # { "image_id": "123e4567-e89b-12d3-a456-426614174000" }
```

2. **Retrieve an Image**
- **Endpoint**: GET /image/<image_id>
- **Description**: Retrieve an image using its unique image_id.
- **Request Format**:
  - URL Parameter: image_id
- **Response Format**:
  - Image file in PNG format
- **Example Request**:

```py
    import requests
    
    image_id = "123e4567-e89b-12d3-a456-426614174000"
    url = f"http://127.0.0.1:1234/image/{image_id}"
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
      with open("retrieved_image.png", "wb") as file:
          for chunk in response.iter_content(1024):
              file.write(chunk)
      print("Image saved as retrieved_image.png")
    else:
      print("Error:", response.json())
```

## UML Sequence Diagram
Below is the UML sequence diagram illustrating the interaction with the microservice:

```
User               Microservice
 |                      |
 |----POST /upload----->|  (User uploads an image)
 |                      |
 |<---- 201 Created ----|  (Microservice returns image_id)
 |                      |
 |----GET /image/{id}-->|  (User requests image by ID)
 |                      |
 |<--- 200 OK (image)---|  (Microservice returns image)
```
---
### Notes
- Ensure the microservice is running before making requests.
- Images are stored in the 'uploads' directory.
- Only PNG and JPG image formats are supported.