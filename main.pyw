import sys
import cv2
import time
import datetime
import decouple
import schedule
import threading
import screeninfo
from playsound import playsound


def image_jumpscare():
    # Configurando propriedades da janela da imagem
    screen = screeninfo.get_monitors()[0]
    window_name = 'BUU'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

    # Abrindo imagem
    OPEN_SECONDS = decouple.config('SOUND_SECONDS') * 1000

    img = cv2.imread(decouple.config('IMAGE_PATH'))
    cv2.imshow(window_name, img)
    cv2.waitKey(OPEN_SECONDS)
    sys.exit()

def song_jumpscare():
    time.sleep(0.1)
    playsound(decouple.config('SOUND_PATH'))

def main():
    image_thread = threading.Thread(target=image_jumpscare)
    song_thread = threading.Thread(target=song_jumpscare)

    image_thread.start()
    song_thread.start()
    image_thread.join()
    song_thread.join()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # main()
    jumpscare_time: str = decouple.config('JUMPSCARE_TIME')

    # Se estiver vazio, seta o tempo para daqui 1 minuto.
    if not time:
        jumpscare_time = datetime.datetime.strftime(
            datetime.datetime.now() + datetime.timedelta(minutes=1), '%H:%M')
        
    try:
        print(f'Jumpscare programado para: {jumpscare_time}')
        schedule.every().day.at(jumpscare_time).do(main)
        while schedule.get_jobs()[0].last_run is None:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print('Houve um erro no jumpscare')
        raise e
