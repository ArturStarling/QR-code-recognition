import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
# to use buttons:
from kivy.uix.button import Button
from kivy.storage.jsonstore import JsonStore
import cv2

kivy.require("1.11.1")

# add the following 2 lines to solve OpenGL 2.0 bug
from kivy import Config
Config.set('graphics', 'multisamples', '0')


#Storage

store = JsonStore('hello.json')

# put some values
store.put('tito', name='Mathieu', org='kivy', age=30, height=1.80, estate='São Paulo', country='Brasil')
store.put('tshirtman', name='Gabriel', age=27)
store.put('resistor', armario='armário 1', gaveta='gaveta 4', lugar='do lado da caixa laranja', imagem='pinguim.jpg')



class ConnectPage(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2  # used for our grid

        self.add_widget(Label(text='digite o objeto a ser procurado aqui:'))  # widget #1, top left
        self.ip = TextInput(multiline=False)  # defining self.ip...
        self.add_widget(self.ip) # widget #2, top right

        self.add_widget(Label(text='Port:'))
        self.add_widget(Label())

        self.add_widget(Label())
        self.add_widget(Label())

        # add our button.
        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.join)

        self.add_widget(Label())

    def join_button(self, instance):
        #im = cv2.imread("pinguim.jpg")
        #qrDecoder = cv2.QRCodeDetector()
        #data,bbox,rectifiedImage = qrDecoder.detectAndDecode(im)
        print('o objeto está no', store.get('resistor')['armario'], store.get('resistor')['gaveta'], store.get('resistor')['lugar'])
        image = cv2.imread(store.get('resistor')['imagem'])
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()






class EpicApp(App):
    def build(self):
        return ConnectPage()



EpicApp().run()




store = JsonStore('hello.json')

# put some values
store.put('tito', name='Mathieu', org='kivy', age=30, height=1.80, estate='São Paulo', country='Brasil')
store.put('tshirtman', name='Gabriel', age=27)
store.put('resistor', armario='armário 1', gaveta='gaveta 4', lugar='do lado da caixa laranja', imagem='miseravel.jpg')

# using the same index key erases all previously added key-value pairs
#store.put('tito', name='Adriel', age=10)

# get a value using a index key and key

print('o objeto está no', store.get('resistor')['armario'], store.get('resistor')['gaveta'], store.get('resistor')['lugar'])
image = cv2.imread(store.get('resistor')['imagem'])
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()