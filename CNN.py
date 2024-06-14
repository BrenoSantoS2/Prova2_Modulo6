import cv2
from ultralytics import YOLO

# Caminho para o vídeo
video_path = 'la_cabra.mp4'

# Caminho para o modelo YOLOv8
model_path = 'yolov8n-face.pt'

# Carregar o modelo YOLOv8
model = YOLO(model_path)

# Função para detectar rostos em um frame
def detect_faces(frame):
    results = model(frame)
    return results

# Captura de vídeo
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Erro ao abrir o arquivo de vídeo.")
else:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detectar rostos no frame
        results = detect_faces(frame)
        
        # Desenhar caixas delimitadoras ao redor dos rostos detectados
        for result in results:
            for bbox in result.boxes:
                x1, y1, x2, y2 = map(int, bbox.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Exibir o frame com as detecções
        cv2.imshow('Frame', frame)
        
        # Pressione 'q' no teclado para sair do vídeo
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Libere a captura de vídeo e feche todas as janelas
    cap.release()
    cv2.destroyAllWindows()
