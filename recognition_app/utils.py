from mtcnn import MTCNN
from deepface import DeepFace
import numpy as np
import os

detector = MTCNN()

def detect_faces(image):
    faces = detector.detect_faces(image)
    return [image[y:y+h, x:x+w] for (x, y, w, h) in [face["box"] for face in faces]]

def extract_features(faces):
    embeddings = []
    for face in faces:
        embedding = DeepFace.represent(face, model_name="Facenet")
        embeddings.append(embedding)
    return embeddings

def match_faces(embeddings):
    results = []
    for embedding in embeddings:
        best_match = None
        best_score = 0
        for known_file in os.listdir("data/embeddings/"):
            known_embedding = np.load(os.path.join("data/embeddings/", known_file))
            similarity = np.dot(embedding, known_embedding) / (np.linalg.norm(embedding) * np.linalg.norm(known_embedding))
            if similarity > best_score:
                best_score = similarity
                best_match = known_file.split(".")[0]
        results.append({"match": best_match, "score": float(best_score)})
    return results