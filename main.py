import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen

a = ""
b = ""
c = ""
e = ""
d = ""


def scriptedIn(key, pres):
    print("9")
    alf = "6]?qXsi3JI(y%*t!)E1#=O5eM.~<S$0&7PomQWLFuHY^vap|+b,V:_rCdl@2KUhA;}Z>wT-`9{BNk[zn8DGRxfj/gc4"
    alfT = ""
    """
    i = 0
    while len(alfT) > i:
        rand = random.randint(0, len(alfT)-1)
        alf += alfT[rand]
        alfT = alfT.replace(alfT[rand], "")
    print(alf)
    """
    pres = int(pres)

    if pres == 0:
        now = datetime.datetime.now()
        h = int(now.strftime("%H"))
        m = int(now.strftime("%M"))
        pres = m * h

    keyTemp = ""
    i = 0

    while len(key) > i:
        poz = alf.index(key[i])
        poz += pres
        poz = poz % len(alf)
        keyTemp += alf[poz]
        i += 1
    return keyTemp, pres


def scriptedOut(keyTemp, pres):
    print("10")
    alf = "6]?qXsi3JI(y%*t!)E1#=O5eM.~<S$0&7PomQWLFuHY^vap|+b,V:_rCdl@2KUhA;}Z>wT-`9{BNk[zn8DGRxfj/gc4"
    key = ""
    pres = int(pres)
    i = 0
    while len(keyTemp) > i:
        poz = alf.index(keyTemp[i])
        poz -= pres
        poz = poz % len(alf)
        key += alf[poz]
        i += 1
    """
    print(pres)
    jj = 0
    while jj < len(key):
        i = 0
        while len(alf) > i:
            if key[jj] == alf[i]:
                print(i)
                print("key     : " + str(jj) + " - " + key[jj] + " --- " + str(alf.index(key[jj])-alf.index(keyTemp[jj])) + " ---- "+ str((pres - poz) % len(alf)))
                print("keyTemp : " + str(jj) + " - " + keyTemp[jj] + " --- " + str(alf.index(keyTemp[jj])-alf.index(key[jj])) + " ---- " + str((abs( pres + 1)) % len(alf)))
            i += 1
        jj += 1
    """
    return key


class MyButton(ButtonBehavior, Image):
    print("11")

    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = 'atlas://data/images/defaulttheme/checkbox_off'

    def on_press(self):
        self.source = 'atlas://data/images/defaulttheme/checkbox_on'

    def on_release(self):
        self.source = 'atlas://data/images/defaulttheme/checkbox_off'


def openFile(nameFile):
    print("12")
    try:
        file = open(nameFile, "r")
        temps = file.readlines()
        file.close()
        ListTemp = []
        i = 0
        while i < len(temps):
            temp = temps[i].replace("\n", "")
            temp = temp.split(" ")
            ListTemp.append(temp)
            i += 1
        return True, ListTemp
    except:
        return False


class RV(RecycleView):
    print("13")

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        try:
            file = openFile("conf")
            ListTemp = []
            i = 1
            if not file[0]:
                print("Blad pliku")
                file = open("conf", "w+")
                file.close()
                self.data = [{'text': "Error", 'ind': 0, 'selected': 1}]
            else:
                while i < len(file[1]) - 1:
                    ListTemp.append(file[1][i])
                    i += 1
                    globals.ListKey = ListTemp

                self.data = [{'text': str(ListTemp[x][0] + " " + ListTemp[x][1] + " " + ListTemp[x][2]),
                              'ind': int(ListTemp[x][0]) - 1, 'selected': 0} for x in range(len(ListTemp))]
                self.ids.name_part.text = "all"
        except:
            pass


class TestBox(BoxLayout):
    print("14")

    def action(self, boss):
        self.ids.passwd_part.text = boss.data[self.ind]['text']
        if boss.data[self.ind]['selected'] == 0:
            print(boss.data[self.ind]['text'])
            boss.data[self.ind]['selected'] = 1
            Tab = boss.data[self.ind]['text'].split(" ")
            globals.pos = str(Tab[0])
            globals.name = str(Tab[1])
            globals.key = str(Tab[2])
            show_popup()
        else:
            boss.data[self.ind]['selected'] = 0


def show_popup():
    show = Popups()
    print("15")
    popupWindow = Popup(title="Edytor hasel", content=show,
                        size_hint=(None, None), size=(200, 300))
    # open popup window

    popupWindow.open()
    # bind the on_press event of the button to the dismiss function
    # Attach close button press with popup.dismiss action
    # content.bind(on_press = popup.dismiss())

    return popupWindow


class MainWindow(Screen):
    print("16")
    pass


class LogonWindow(Screen):
    login__ = ObjectProperty(None)
    passwd__ = ObjectProperty(None)
    print("1")

    def check(self):
        try:
            file = open("configuration.conf", "r")
            print("File is ok. {Info-conf_0} ")
        except:
            file = open("configuration.conf", "w+")
            file.write("conf 39 True True True")
            file.close()
            print("Create new file [conf 5 True True True]")
            file = open("configuration.conf", "r")
        temps = file.readlines()
        file.close()
        temp = temps[0].replace("\n", "")
        temp = temp.split(" ")
        temp = openFile(temp[0])

        if temp == 0:
            _key_ = scriptedIn("admin", 0)
            file = open("conf", "w+")
            file.write(_key_[0] + " " + str(_key_[1]))
            file.close()
            temp = openFile("conf")

        key_od = scriptedOut(temp[1][0][0], temp[1][0][1])
        if "admin" == self.ids.login__.text and key_od == self.ids.passwd__.text:
            self.parent.current = "main"
            self.ids.passwd__.text = ""
        else:
            show = PopupsLogon()
            popupWindow = Popup(title="Date error", content=show,
                                size_hint=(None, None), size=(200, 120))
            popupWindow.open()


class PopupsLogon(FloatLayout):
    print("2")
    pass


class Popups(FloatLayout):
    print("3")
    editPasswordPopup = ObjectProperty(None)
    editNamePopup = ObjectProperty(None)
    editposPopup = ObjectProperty(None)

    def refresh(self):
        self.ids.editposPopup.text = globals.pos
        self.ids.editNamePopup.text = globals.name
        self.ids.editPasswordPopup.text = globals.key

    def hulk_smash(self):
        self.ids.hulk.text = "hulk: puny god!"
        self.ids["loki"].text = "loki: >_<!!!"  # alternative syntax

    def btn(self):
        if self.editposPopup.text != "" and self.editNamePopup.text != "" and self.editPasswordPopup.text != "":
            file = open("confi", "r")
            temps = file.readlines()
            file.close()
            ListTemp = []
            Change = True
            i = 0

            while i < len(temps):
                temp = temps[i].replace("\n", "")
                temp = temp.split(" ")
                ListTemp.append(temp)
                i += 1

            i = 1
            while len(ListTemp) > i:
                if ListTemp[i][0] == self.editposPopup.text:
                    ListTemp[i][2] = self.editPasswordPopup.text
                    ListTemp[i][1] = self.editNamePopup.text
                    Change = False
                i += 1

            i = 1
            file = open("confi", "w+")
            file.write(ListTemp[0][0] + " " + ListTemp[0][1])
            while i < len(ListTemp):
                file.write("\n" + ListTemp[i][0] + " " + ListTemp[i][1] + " " + ListTemp[i][2])
                i += 1
            if Change:
                file.write(
                    "\n" + self.editposPopup.text + " " + self.editNamePopup.text + " " + self.editPasswordPopup.text)
            file.close()
            print(self.editPasswordPopup.text + self.editNamePopup.text + self.editposPopup.text)

    def delete(self):
        if self.editposPopup.text != "":
            file = open("confi", "r")
            temps = file.readlines()
            file.close()
            ListTemp = []
            Change = True
            i = 0

            while i < len(temps):
                temp = temps[i].replace("\n", "")
                temp = temp.split(" ")
                ListTemp.append(temp)
                i += 1

            i = 1
            while len(ListTemp) > i:
                if ListTemp[i][0] == self.editposPopup.text:
                    ListTemp.remove(ListTemp[i])
                    Change = False
                i += 1

            i = 1
            file = open("confi", "w+")
            file.write(ListTemp[0][0] + " " + ListTemp[0][1])
            while i < len(ListTemp):
                file.write("\n" + ListTemp[i][0] + " " + ListTemp[i][1] + " " + ListTemp[i][2])
                i += 1
            file.close()


class EditCreatePasswordWindow(Screen):
    print("4")
    WindowPopup = None

    def btn(self):
        # calling of the show popup function
        WindowPopup = show_popup()
        # WindowPopup.dismiss()
        i = 0

    def refresh_(self):
        # self.ids.name_part.text = "All"
        EditCreatePasswordWindow()


class PopupsNewApt(FloatLayout):
    print("5")
    pass


class ConfigurationWindow(Screen):
    print("6")

    def refresh_(self):
        try:
            file = open("configuration.conf", "r")
            print("File is ok. {Info-conf_0} ")
        except:
            file = open("configuration.conf", "w+")
            file.write("conf 39 True True True")
            file.close()
            print("Create new file [conf 39 True True True]")
            file = open("configuration.conf", "r")
        temps = file.readlines()
        file.close()
        temp = temps[0].replace("\n", "")
        temp = temp.split(" ")

        self.ids.name_file.text = temp[0]
        self.ids.fileNameCode.text = temp[0]
        self.ids.changePassword_1.text = "***"
        self.ids.changePassword_2.text = "***"
        self.ids.slider_size_gen_pass_Slider.text = temp[1]
        self.ids.Slider_.text = temp[1]
        if not temp[2]:
            self.ids.YesLogonAccept.background_color = (0.0, 1.0, 0.0, 1.0)
            self.ids.NoLogonAccept.background_color = (1.0, 1.0, 1.0, 1.0)
        else:
            self.ids.NoLogonAccept.background_color = (0.0, 1.0, 0.0, 1.0)
            self.ids.YesLogonAccept.background_color = (1.0, 1.0, 1.0, 1.0)

    def pressYesTrue(self):
        self.ids.YesLogonAccept.background_color = (0.0, 1.0, 0.0, 1.0)
        self.ids.NoLogonAccept.background_color = (1.0, 1.0, 1.0, 1.0)

    def pressNoTrue(self):
        self.ids.NoLogonAccept.background_color = (0.0, 1.0, 0.0, 1.0)
        self.ids.YesLogonAccept.background_color = (1.0, 1.0, 1.0, 1.0)

    def save(self):
        try:
            file = open("configuration.conf", "r")
            print("File is ok. {Info-conf_0} ")
        except:
            file = open("configuration.conf", "w+")
            file.write("conf 39 True True True")
            file.close()
            print("Create new file [conf 39 True True True]")
            file = open("configuration.conf", "r")
        temps = file.readlines()
        file.close()
        temp = temps[0].replace("\n", "")
        temp = temp.split(" ")
        A = False
        file = open("configuration.conf", "r")
        temps = file.readlines()
        file.close()
        file = open("configuration.conf", "w+")
        avc = self.ids.YesLogonAccept.background_color
        if self.ids.YesLogonAccept.background_color == [0.0, 1.0, 0.0, 1.0]:
            A = True
        if self.ids.NoLogonAccept.background_color == [0.0, 1.0, 0.0, 1.0]:
            A = False

        file.write(
            self.ids.fileNameCode.text + " " + self.ids.slider_size_gen_pass_Slider.text + " " + str(
                A) + " False False")
        file.close()
        file = open("configuration.conf", "r")

        print("Date save info: ")
        print("Name: ", self.ids.fileNameCode.text)
        print("SizeKey: ", self.ids.slider_size_gen_pass_Slider.text)
        print("NoLogon: ", str(A))

    def check_status(self, btn):
        def register(self):
            print("user: ", self.ids.user_input.text)
            print("password: ", self.ids.password_input.text)

        a = self.fileName

    def save_passwd(self):

        if self.ids.changePassword_1.text != "" and self.ids.changePassword_2.text != "" and self.ids.changePassword_1.text != "***":
            if self.ids.changePassword_1.text == self.ids.changePassword_2.text:
                try:
                    file = open("configuration.conf", "r")
                    print("File is ok. {Info-conf_0} ")
                except:
                    file = open("configuration.conf", "w+")
                    file.write("conf 39 True True True")
                    file.close()
                    print("Create new file [conf 39 True True True]  {Info-conf_1}")
                    file = open("configuration.conf", "r")
                temps = file.readlines()
                file.close()
                temp = temps[0].replace("\n", "")
                temp = temp.split(" ")
                NameFileConf = temp[0]
                ListTemp = []
                try:
                    file = open(temp[0], "r")
                    temps = file.readlines()
                    file.close()
                    print("File is ok. [key, id_link] {Info-passwdMain_0} ")
                    i = 0
                    while i < len(temps):
                        temp = temps[i].replace("\n", "")
                        temp = temp.split(" ")
                        ListTemp.append(temp)
                        i += 1
                    key_strip = scriptedIn(self.ids.changePassword_1.text, ListTemp[0][1])


                except:
                    key_strip = scriptedIn(self.ids.changePassword_1.text, 0)
                    print("Create new file passwd [key, id_link] {Info-save_conf_1}")

                file = open(NameFileConf, "w+")
                file.write(key_strip[0] + " " + str(key_strip[1]))

                i = 1
                while i < len(ListTemp):
                    file.write(
                        "\n" + ListTemp[i][0] + " " + ListTemp[i][1] + " " + ListTemp[i][2])
                    i += 1
                file.close()
                print("Password has been changed {Info-correctChangedPasswd_0}")
                self.ids.ButtomChangePasswd.background_color = (0.0, 1.0, 0.0, 1.0)
            else:
                self.ids.ButtomChangePasswd.background_color = (1.0, 0.0, 0.0, 1.0)
                print("InputTest  is different {Info-InputTestIsDifferent_1}")
        else:
            self.ids.ButtomChangePasswd.background_color = (1.0, 1.0, 0.0, 1.0)
            print("InputTest is empty {Info-InputTestIsEmpty_1}")


class WindowManager(ScreenManager):
    print("7")
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    print("8")
    editNamePopup_ = a
    editPasswordPopup_ = b
    editposPopup_ = c
    login_ = d
    passwd_ = e
    ok = ""

    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
