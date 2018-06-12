#clicking a point on the screen is a MotionEvent and returns on the command line spos =(x-coord, y-coord) where the lower left is (0,0) and the upper right is (1,1,). It also returns pos=(something, somethingelse), but I don't know what this is.
import kivy

from kivy.app import App
from kivy.uix.widget import Widget


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)


class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()
