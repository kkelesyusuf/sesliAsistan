import speech_recognition as sr
from Core.UI import UI
from Core.Brain import Brain


class Asistan(sr.Recognizer):
    def __init__(self):
        super().__init__()
        ## UI
        self.window = UI()
        self.speak_button = self.window.setup_ui_contents(command=self.awake_assistan)
        self.brain = Brain()

    def start_ui(self):
        self.window.mainloop()

    def print_devices(self):
        from prettytable import PrettyTable

        table = PrettyTable()
        table.title = "AVAILABLE MICROPHONES"
        table.field_names = ["Index", "Device Name"]
        table.add_rows(enumerate(sr.Microphone.list_microphone_names()))
        table.align = "l"
        print(table)

    def __update_btn_lbl(self, is_listening):
        new_text = "Dinliyorum..." if is_listening else "Konuşmak için Bas"
        self.speak_button.config(text=new_text)
        self.speak_button.update()

    def __detect_speech(self):
        try:
            with sr.Microphone() as source:
                self.__update_btn_lbl(True)

                audio = self.listen(source)

                try:
                    new_input = self.recognize_google(audio_data=audio, language="tr_TR")
                except sr.UnknownValueError:
                    print("Söylenilenler anlaşılmadı...")
                except sr.RequestError as e:
                    print("Herhangi bir şey söylenmedi; {0}".format(e))
                else:
                    return new_input
        except:
            self.window.show_mic_error()
        finally:
            self.__update_btn_lbl(False)

    def awake_assistan(self):
        input = self.__detect_speech()

        self.brain.make_sense(input)
