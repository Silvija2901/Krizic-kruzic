from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

# Designate Our .kv design file 
Builder.load_file('try2.kv')
l1=["a","b","c","d","e","f","g","h","i"]

l=["znak0","znak1","znak2","znak3","znak4","znak5","znak6","znak7","znak8"]

x="X"

n=0
class MyLayout(Widget):
    def press(self, button_name):
        global x,l1, n
        if not (l1[button_name]=="X" or l1[button_name]=="O"):
            n=n+1
            if button_name==0:
                self.ids.znak0.text=x
                l1[button_name]=x

            if button_name==1:
                self.ids.znak1.text=x
                l1[button_name]=x
            
            if button_name==2:
                self.ids.znak2.text=x
                l1[button_name]=x
            
            if button_name==3:
                self.ids.znak3.text=x
                l1[button_name]=x
            
            if button_name==4:
                self.ids.znak4.text=x
                l1[button_name]=x
            
            if button_name==5:
                self.ids.znak5.text=x
                l1[button_name]=x
            
            if button_name==6:
                self.ids.znak6.text=x
                l1[button_name]=x
            
            if button_name==7:
                self.ids.znak7.text=x
                l1[button_name]=x
            
            if button_name==8:
                self.ids.znak8.text=x
                l1[button_name]=x
            
        

            if l1[0]==l1[1]==l1[2] or l1[3]==l1[4]==l1[5] or l1[6]==l1[7]==l1[8]:
                print(x, " je pobjedio")
                self.ids.znak0.text=""
                self.ids.znak1.text=""
                self.ids.znak2.text=""
                self.ids.znak3.text=""
                self.ids.znak4.text=""
                self.ids.znak5.text=""
                self.ids.znak6.text=""
                self.ids.znak7.text=""
                self.ids.znak8.text=""
                l1=["a","b","c","d","e","f","g","h","i"]
                n=0
            if l1[0]==l1[3]==l1[6] or l1[1]==l1[4]==l1[7] or l1[2]==l1[5]==l1[8]:
                print(x, " je pobjedio")
                self.ids.znak0.text=""
                self.ids.znak1.text=""
                self.ids.znak2.text=""
                self.ids.znak3.text=""
                self.ids.znak4.text=""
                self.ids.znak5.text=""
                self.ids.znak6.text=""
                self.ids.znak7.text=""
                self.ids.znak8.text=""
                l1=["a","b","c","d","e","f","g","h","i"]
                n=0
            if l1[0]==l1[4]==l1[8] or l1[2]==l1[4]==l1[6]:
                print(x, " je pobjedio")
                self.ids.znak0.text=""
                self.ids.znak1.text=""
                self.ids.znak2.text=""
                self.ids.znak3.text=""
                self.ids.znak4.text=""
                self.ids.znak5.text=""
                self.ids.znak6.text=""
                self.ids.znak7.text=""
                self.ids.znak8.text=""
                l1=["a","b","c","d","e","f","g","h","i"]
                n=0
            if n==9:
                print("Nerješeno")
                self.ids.znak0.text=""
                self.ids.znak1.text=""
                self.ids.znak2.text=""
                self.ids.znak3.text=""
                self.ids.znak4.text=""
                self.ids.znak5.text=""
                self.ids.znak6.text=""
                self.ids.znak7.text=""
                self.ids.znak8.text=""
                l1=["a","b","c","d","e","f","g","h","i"]
                n=0
                
            if x=="X":
                x="O"
            else:
                x="X"


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()

