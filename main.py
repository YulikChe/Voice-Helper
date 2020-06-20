import App3
from opts import options
import speech_recognition as sr
import sys
from fuzzywuzzy import fuzz

def hear():
    r = sr.Recognizer()


    start_was = False

    with sr.Microphone(device_index=1) as sourse:
        r.adjust_for_ambient_noise(sourse, duration=1)
        audio = r.listen(sourse)

    try:
        com = r.recognize_google(audio, language="ru-RU").lower()
        print(com)
        for c in options["call"]:
            if fuzz.ratio(com, c) > 80:
                start_was = True
                App3.maiin()

        if start_was == False:
            hear()
    except sr.UnknownValueError:
        hear()
    except sr.RequestError:
        sys.exit()

hear()