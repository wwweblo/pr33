from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.animation import Animation

class AnimatedWidget(Label):
    def __init__(self, **kwargs):
        super(AnimatedWidget, self).__init__(**kwargs)

    def play_animation(self):
        # Пример анимации - перемещение виджета вправо на 100 пикселей за 1 секунду
        my_animation = Animation(x=self.x + 100, duration=1)
        my_animation.start(self)

class MyApp(App):
    def build(self):
        # Основной макет
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Виджет для анимации
        animated_widget = AnimatedWidget(text='Анимация')
        layout.add_widget(animated_widget)

        # Кнопка для запуска анимации
        button = Button(text='Начать анимацию')
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # Получаем AnimatedWidget из дочерних элементов макета
        animated_widget = None
        for child in self.root.children:
            if isinstance(child, AnimatedWidget):
                animated_widget = child
                break

        if animated_widget:
            # Запускаем анимацию
            animated_widget.play_animation()

if __name__ == '__main__':
    MyApp().run()
