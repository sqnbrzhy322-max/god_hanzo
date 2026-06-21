from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
import os
import shutil

SOURCE_FILE = "/storage/emulated/0/Download/Active.sav"
store = JsonStore("data.json")


class RootUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(Label(text="🔥 GOD HANZO PRO+", font_size=30))

        self.status = Label(text="Ready", font_size=18)
        self.add_widget(self.status)

        self.btn_select = Button(text="📁 Select PUBG Folder (SAF)")
        self.btn_select.bind(on_press=self.select_folder)
        self.add_widget(self.btn_select)

        self.btn_copy = Button(text="⚡ COPY Active.sav")
        self.btn_copy.bind(on_press=self.copy_file)
        self.add_widget(self.btn_copy)

    # در نسخه واقعی SAF اینجا اضافه می‌شود (Buildozer + Android API)
    def select_folder(self, instance):
        path = "/storage/emulated/0/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/SaveGames"
        store.put("path", value=path)
        self.status.text = "Folder Saved ✔"

    def copy_file(self, instance):
        if not os.path.exists(SOURCE_FILE):
            self.status.text = "❌ Active.sav not found"
            return

        if not store.exists("path"):
            self.status.text = "❌ Select folder first"
            return

        dest = store.get("path")["value"]

        try:
            shutil.copy2(SOURCE_FILE, os.path.join(dest, "Active.sav"))
            self.status.text = "✅ COPY SUCCESS"
        except Exception as e:
            self.status.text = f"ERROR: {str(e)}"


class GodHanzo(App):
    def build(self):
        return RootUI()


if __name__ == "__main__":
    GodHanzo().run()