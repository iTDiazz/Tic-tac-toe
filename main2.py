from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRectangleFlatButton


class FirstApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        flag = True
        flag2 = True

        def press_button(self):
            nonlocal flag
            nonlocal flag2
            if flag2:
                if flag and self.text != '0':
                    self.text = "X"
                    flag = False
                elif not flag and self.text != 'X':
                    self.text = '0'
                    flag = True
            cell = layout.children # В children записываются все добавленные виджеты
            for i in cell:
                if cell[0].text == cell[1].text == cell[2].text and cell[0].text != '':
                    cell[0].md_bg_color = cell[1].md_bg_color = cell[2].md_bg_color = (1, 0, 0, 0.5)
                    flag2 = False
                elif cell[3].text == cell[4].text == cell[5].text and cell[3].text != '':
                    cell[3].md_bg_color = cell[4].md_bg_color = cell[5].md_bg_color = (1, 0, 0, 0.5)
                    flag2 = False
                elif cell[6].text == cell[7].text == cell[8].text and cell[6].text != '':
                    cell[6].md_bg_color = cell[7].md_bg_color = cell[8].md_bg_color = (1, 0, 0, 0.5)
                    flag2 = False
                elif cell[0].text == cell[3].text == cell[6].text and cell[0].text != '':
                    cell[0].md_bg_color = cell[3].md_bg_color = cell[6].md_bg_color = (1, 0, 0, 0.5)
                    flag2 = False
                elif cell[1].text == cell[4].text == cell[7].text and cell[1].text != '':
                    cell[1].md_bg_color = cell[4].md_bg_color = cell[7].md_bg_color = (1, 0, 0, 0.5)
                    flag2 = False
                elif cell[2].text == cell[5].text == cell[8].text and cell[2].text != '':
                    cell[2].md_bg_color = cell[5].md_bg_color = cell[8].md_bg_color = (1, 0, 0, 0.5)
                    flag2 = False
                elif cell[0].text == cell[4].text == cell[8].text and cell[0].text != '':
                    cell[0].md_bg_color = cell[4].md_bg_color = cell[8].md_bg_color = (1, 0, 0, 0.5)
                    flag2 = False
                elif cell[2].text == cell[4].text == cell[6].text and cell[2].text != '':
                    cell[2].md_bg_color = cell[4].md_bg_color = cell[6].md_bg_color = (1, 0, 0, 0.5)
                    flag2 = False

        layout = MDGridLayout(cols=3, rows=3)
        for i in range(9):
            but = MDRectangleFlatButton(size_hint=(1/3, 1/3), font_size=150, on_press=press_button)

            layout.add_widget(but)

        return layout


FirstApp().run()