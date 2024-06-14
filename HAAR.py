import cv2
import os

# Caminho para o vídeo e classificador
video_path = 'la_cabra.mp4'
smile_cascade_path = 'haarcascade_smile.xml'
eye_cascade_path = 'haarcascade_eye.xml'

# Captura do vídeo
cap = cv2.VideoCapture(video_path)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('HAAR.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

# Carregar o classificador Haar Cascade
smile_cascade = cv2.CascadeClassifier(smile_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)


# Verifica se o vídeo e o classificador foram carregados com sucesso
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
elif smile_cascade.empty():
    print("Erro ao carregar o classificador Haar Cascade.")
elif eye_cascade.empty():
    print("Erro ao carregar o classificador Haar Cascade.")
else:
    frame_count = 0
    while True:
        # Lê o frame do vídeo
        ret, frame = cap.read()
        
        # Se não conseguiu ler o frame, termina o loop
        if not ret:
            break
        
        # Converter o frame para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detectar rostos
        smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=10, minSize=(60, 60))
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(30, 30))
        
        # Desenhar retângulos ao redor dos rostos detectados
        for (x, y, w, h) in smiles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        

        out.write(frame)

        # Exibir o frame com rostos detectados
        cv2.imshow('Frame', frame)
        
        # Espera 1 ms e verifica se a tecla 'q' foi pressionada para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        frame_count += 1

# Libera o objeto de captura e fecha todas as janelas
out.release()
cap.release()

cv2.destroyAllWindows()
