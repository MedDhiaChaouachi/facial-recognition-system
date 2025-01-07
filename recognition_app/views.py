from django.shortcuts import render
from django.http import JsonResponse
from .utils import detect_faces, extract_features, match_faces
import cv2
import numpy as np

def home(request):
    return render(request, "recognition_app/index.html")

def recognize(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Step 1: Detect faces
        faces = detect_faces(image)
        if not faces:
            return JsonResponse({"error": "No faces detected"}, status=400)

        # Step 2: Extract features
        embeddings = extract_features(faces)

        # Step 3: Match faces
        results = match_faces(embeddings)

        return JsonResponse({"results": results})
    return JsonResponse({"error": "No file uploaded"}, status=400)