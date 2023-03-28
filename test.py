from pywinauto import Application

app = Application(backend='uia').connect(title='无标题 - 记事本')
app.UntitledNotepad.menu_select('格式(O)->字体(F)...')  # 弹出字体设置窗口

# 定位弹出窗口
font_window = app.window(title='字体(F)...')

# 定位控件并点击
font_window.child_window(title='粗体', control_type='ListItem').click()

# 点击确定按钮
font_window['确定'].click()
