import logging
import traceback
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.carousel import Carousel
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, ActionButton
from kivy.uix.splitter import Splitter
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.modalview import ModalView
from kivy.uix.settings import Settings
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.logger import Logger
from kivy.metrics import dp
from functools import partial

# 配置日志
logging.basicConfig(level=logging.DEBUG)
Logger.setLevel(logging.DEBUG)

class KivyUIDemo(App):
    def build(self):
        try:
            Logger.info("KivyUIDemo: 开始构建UI演示应用")
            
            # 创建主屏幕管理器
            sm = ScreenManager()
            
            # 添加各种演示屏幕
            sm.add_widget(self.create_main_screen())
            sm.add_widget(self.create_basic_widgets_screen())
            sm.add_widget(self.create_layout_screen())
            sm.add_widget(self.create_input_screen())
            sm.add_widget(self.create_media_screen())
            sm.add_widget(self.create_advanced_screen())
            
            Logger.info("KivyUIDemo: UI演示应用构建成功")
            return sm
            
        except Exception as e:
            Logger.error(f"KivyUIDemo: 构建应用时发生错误: {str(e)}")
            Logger.error(f"KivyUIDemo: 错误详情: {traceback.format_exc()}")
            return Label(text="应用启动失败，请检查日志")
    
    def create_main_screen(self):
        """创建主屏幕"""
        screen = Screen(name='main')
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # 标题
        title = Label(
            text='Kivy UI 组件演示',
            font_size='24sp',
            size_hint_y=None,
            height=dp(60),
            color=(0.2, 0.6, 1, 1)
        )
        layout.add_widget(title)
        
        # 导航按钮
        nav_buttons = [
            ('基础组件', 'basic_widgets'),
            ('布局管理', 'layout'),
            ('输入组件', 'input'),
            ('媒体组件', 'media'),
            ('高级组件', 'advanced')
        ]
        
        for text, screen_name in nav_buttons:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=dp(50),
                background_color=(0.3, 0.7, 0.9, 1)
            )
            btn.bind(on_press=partial(self.switch_screen, screen_name))
            layout.add_widget(btn)
        
        screen.add_widget(layout)
        return screen
    
    def create_basic_widgets_screen(self):
        """创建基础组件演示屏幕"""
        screen = Screen(name='basic_widgets')
        
        # 使用滚动视图
        scroll = ScrollView()
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10), size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        # 标题
        title = Label(
            text='基础组件演示',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            color=(1, 0.5, 0, 1)
        )
        layout.add_widget(title)
        
        # 各种标签
        labels = [
            ('普通标签', '16sp', (1, 1, 1, 1)),
            ('大号标签', '20sp', (0, 1, 0, 1)),
            ('彩色标签', '18sp', (1, 0, 1, 1))
        ]
        
        for text, font_size, color in labels:
            label = Label(
                text=text,
                font_size=font_size,
                color=color,
                size_hint_y=None,
                height=dp(40)
            )
            layout.add_widget(label)
        
        # 各种按钮
        buttons = [
            ('普通按钮', (0.2, 0.6, 1, 1)),
            ('绿色按钮', (0.2, 0.8, 0.2, 1)),
            ('红色按钮', (0.8, 0.2, 0.2, 1))
        ]
        
        for text, color in buttons:
            btn = Button(
                text=text,
                background_color=color,
                size_hint_y=None,
                height=dp(50)
            )
            btn.bind(on_press=partial(self.show_popup, f'{text}被点击了！'))
            layout.add_widget(btn)
        
        # 进度条
        progress_label = Label(
            text='进度条演示',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(progress_label)
        
        self.progress_bar = ProgressBar(
            max=100,
            value=30,
            size_hint_y=None,
            height=dp(20)
        )
        layout.add_widget(self.progress_bar)
        
        # 启动进度条动画
        Clock.schedule_interval(self.update_progress, 0.1)
        
        # 返回按钮
        back_btn = Button(
            text='返回主页',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.5, 0.5, 0.5, 1)
        )
        back_btn.bind(on_press=partial(self.switch_screen, 'main'))
        layout.add_widget(back_btn)
        
        scroll.add_widget(layout)
        screen.add_widget(scroll)
        return screen
    
    def create_layout_screen(self):
        """创建布局管理演示屏幕"""
        screen = Screen(name='layout')
        main_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # 标题
        title = Label(
            text='布局管理演示',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            color=(1, 0.5, 0, 1)
        )
        main_layout.add_widget(title)
        
        # 网格布局演示
        grid_label = Label(
            text='网格布局 (GridLayout)',
            size_hint_y=None,
            height=dp(30)
        )
        main_layout.add_widget(grid_label)
        
        grid = GridLayout(cols=3, size_hint_y=None, height=dp(120), spacing=dp(5))
        for i in range(9):
            btn = Button(
                text=f'G{i+1}',
                background_color=(0.3 + i*0.08, 0.5, 0.8, 1)
            )
            grid.add_widget(btn)
        main_layout.add_widget(grid)
        
        # 水平布局演示
        h_label = Label(
            text='水平布局 (BoxLayout)',
            size_hint_y=None,
            height=dp(30)
        )
        main_layout.add_widget(h_label)
        
        h_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), spacing=dp(5))
        for i, color in enumerate([(1, 0.3, 0.3, 1), (0.3, 1, 0.3, 1), (0.3, 0.3, 1, 1)]):
            btn = Button(
                text=f'H{i+1}',
                background_color=color
            )
            h_layout.add_widget(btn)
        main_layout.add_widget(h_layout)
        
        # 浮动布局演示
        float_label = Label(
            text='浮动布局 (FloatLayout)',
            size_hint_y=None,
            height=dp(30)
        )
        main_layout.add_widget(float_label)
        
        float_layout = FloatLayout(size_hint_y=None, height=dp(150))
        
        # 添加背景色
        with float_layout.canvas.before:
            Color(0.1, 0.1, 0.1, 1)
            Rectangle(pos=float_layout.pos, size=float_layout.size)
        
        positions = [
            {'pos_hint': {'x': 0.1, 'y': 0.7}, 'size_hint': (0.2, 0.2)},
            {'pos_hint': {'x': 0.4, 'y': 0.4}, 'size_hint': (0.2, 0.2)},
            {'pos_hint': {'x': 0.7, 'y': 0.1}, 'size_hint': (0.2, 0.2)}
        ]
        
        for i, pos_info in enumerate(positions):
            btn = Button(
                text=f'F{i+1}',
                background_color=(0.8, 0.4 + i*0.2, 0.6, 1),
                **pos_info
            )
            float_layout.add_widget(btn)
        
        main_layout.add_widget(float_layout)
        
        # 返回按钮
        back_btn = Button(
            text='返回主页',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.5, 0.5, 0.5, 1)
        )
        back_btn.bind(on_press=partial(self.switch_screen, 'main'))
        main_layout.add_widget(back_btn)
        
        screen.add_widget(main_layout)
        return screen
    
    def create_input_screen(self):
        """创建输入组件演示屏幕"""
        screen = Screen(name='input')
        
        scroll = ScrollView()
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10), size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        # 标题
        title = Label(
            text='输入组件演示',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            color=(1, 0.5, 0, 1)
        )
        layout.add_widget(title)
        
        # 文本输入
        text_label = Label(
            text='文本输入框:',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(text_label)
        
        text_input = TextInput(
            text='请输入文本...',
            multiline=False,
            size_hint_y=None,
            height=dp(40)
        )
        layout.add_widget(text_input)
        
        # 多行文本输入
        multiline_label = Label(
            text='多行文本输入:',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(multiline_label)
        
        multiline_input = TextInput(
            text='这是多行文本输入框\n可以输入多行内容',
            multiline=True,
            size_hint_y=None,
            height=dp(80)
        )
        layout.add_widget(multiline_input)
        
        # 滑块
        slider_label = Label(
            text='滑块控件:',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(slider_label)
        
        self.slider_value_label = Label(
            text='值: 50',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(self.slider_value_label)
        
        slider = Slider(
            min=0,
            max=100,
            value=50,
            size_hint_y=None,
            height=dp(40)
        )
        slider.bind(value=self.on_slider_value)
        layout.add_widget(slider)
        
        # 复选框
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
        checkbox_layout.add_widget(Label(text='复选框:'))
        
        checkbox = CheckBox(active=True, size_hint_x=None, width=dp(50))
        checkbox.bind(active=self.on_checkbox_active)
        checkbox_layout.add_widget(checkbox)
        
        self.checkbox_label = Label(text='已选中')
        checkbox_layout.add_widget(self.checkbox_label)
        
        layout.add_widget(checkbox_layout)
        
        # 开关
        switch_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
        switch_layout.add_widget(Label(text='开关:'))
        
        switch = Switch(active=False, size_hint_x=None, width=dp(80))
        switch.bind(active=self.on_switch_active)
        switch_layout.add_widget(switch)
        
        self.switch_label = Label(text='关闭')
        switch_layout.add_widget(self.switch_label)
        
        layout.add_widget(switch_layout)
        
        # 下拉选择器
        spinner_label = Label(
            text='下拉选择器:',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(spinner_label)
        
        spinner = Spinner(
            text='选择选项',
            values=['选项1', '选项2', '选项3', '选项4'],
            size_hint_y=None,
            height=dp(40)
        )
        spinner.bind(text=self.on_spinner_select)
        layout.add_widget(spinner)
        
        self.spinner_result = Label(
            text='未选择',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(self.spinner_result)
        
        # 返回按钮
        back_btn = Button(
            text='返回主页',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.5, 0.5, 0.5, 1)
        )
        back_btn.bind(on_press=partial(self.switch_screen, 'main'))
        layout.add_widget(back_btn)
        
        scroll.add_widget(layout)
        screen.add_widget(scroll)
        return screen
    
    def create_media_screen(self):
        """创建媒体组件演示屏幕"""
        screen = Screen(name='media')
        
        scroll = ScrollView()
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10), size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        # 标题
        title = Label(
            text='媒体组件演示',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            color=(1, 0.5, 0, 1)
        )
        layout.add_widget(title)
        
        # 图像占位符（由于没有实际图片文件）
        image_label = Label(
            text='图像组件 (Image)',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(image_label)
        
        # 创建一个带背景色的标签作为图像占位符
        image_placeholder = Label(
            text='图像占位符\n(实际应用中可加载图片)',
            size_hint_y=None,
            height=dp(100),
            color=(1, 1, 1, 1)
        )
        
        with image_placeholder.canvas.before:
            Color(0.3, 0.6, 0.9, 1)
            Rectangle(pos=image_placeholder.pos, size=image_placeholder.size)
        
        layout.add_widget(image_placeholder)
        
        # 颜色选择器
        color_label = Label(
            text='颜色选择器 (ColorPicker)',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(color_label)
        
        color_picker = ColorPicker(
            size_hint_y=None,
            height=dp(200)
        )
        color_picker.bind(color=self.on_color_change)
        layout.add_widget(color_picker)
        
        self.color_result = Label(
            text='选择的颜色: RGB(1.0, 1.0, 1.0)',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(self.color_result)
        
        # 文件选择器
        file_label = Label(
            text='文件选择器 (FileChooser)',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(file_label)
        
        file_chooser = FileChooserListView(
            size_hint_y=None,
            height=dp(200)
        )
        file_chooser.bind(selection=self.on_file_select)
        layout.add_widget(file_chooser)
        
        self.file_result = Label(
            text='未选择文件',
            size_hint_y=None,
            height=dp(30)
        )
        layout.add_widget(self.file_result)
        
        # 返回按钮
        back_btn = Button(
            text='返回主页',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.5, 0.5, 0.5, 1)
        )
        back_btn.bind(on_press=partial(self.switch_screen, 'main'))
        layout.add_widget(back_btn)
        
        scroll.add_widget(layout)
        screen.add_widget(scroll)
        return screen
    
    def create_advanced_screen(self):
        """创建高级组件演示屏幕"""
        screen = Screen(name='advanced')
        
        # 使用选项卡面板
        tab_panel = TabbedPanel(do_default_tab=False)
        
        # 手风琴选项卡
        accordion_tab = TabbedPanelItem(text='手风琴')
        accordion = Accordion()
        
        for i in range(3):
            item = AccordionItem(title=f'手风琴项目 {i+1}')
            content = BoxLayout(orientation='vertical', padding=dp(10))
            content.add_widget(Label(text=f'这是手风琴项目 {i+1} 的内容'))
            content.add_widget(Button(text=f'按钮 {i+1}', size_hint_y=None, height=dp(40)))
            item.add_widget(content)
            accordion.add_widget(item)
        
        accordion_tab.add_widget(accordion)
        tab_panel.add_widget(accordion_tab)
        
        # 轮播图选项卡
        carousel_tab = TabbedPanelItem(text='轮播图')
        carousel = Carousel(direction='right')
        
        colors = [(1, 0.3, 0.3, 1), (0.3, 1, 0.3, 1), (0.3, 0.3, 1, 1), (1, 1, 0.3, 1)]
        for i, color in enumerate(colors):
            slide = Label(
                text=f'轮播页面 {i+1}\n左右滑动切换',
                color=(0, 0, 0, 1) if i == 3 else (1, 1, 1, 1)
            )
            with slide.canvas.before:
                Color(*color)
                Rectangle(pos=slide.pos, size=slide.size)
            carousel.add_widget(slide)
        
        carousel_tab.add_widget(carousel)
        tab_panel.add_widget(carousel_tab)
        
        # 分割器选项卡
        splitter_tab = TabbedPanelItem(text='分割器')
        splitter = Splitter(sizable_from='right')
        
        left_panel = BoxLayout(orientation='vertical', padding=dp(10))
        left_panel.add_widget(Label(text='左侧面板'))
        left_panel.add_widget(Button(text='左侧按钮', size_hint_y=None, height=dp(40)))
        
        right_panel = BoxLayout(orientation='vertical', padding=dp(10))
        right_panel.add_widget(Label(text='右侧面板\n可拖拽分割线调整大小'))
        right_panel.add_widget(Button(text='右侧按钮', size_hint_y=None, height=dp(40)))
        
        splitter.add_widget(left_panel)
        splitter.add_widget(right_panel)
        
        splitter_tab.add_widget(splitter)
        tab_panel.add_widget(splitter_tab)
        
        # 控制选项卡
        control_tab = TabbedPanelItem(text='控制')
        control_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # 弹窗按钮
        popup_btn = Button(
            text='显示弹窗',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.8, 0.4, 0.8, 1)
        )
        popup_btn.bind(on_press=self.show_custom_popup)
        control_layout.add_widget(popup_btn)
        
        # 模态视图按钮
        modal_btn = Button(
            text='显示模态视图',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.4, 0.8, 0.8, 1)
        )
        modal_btn.bind(on_press=self.show_modal_view)
        control_layout.add_widget(modal_btn)
        
        # 气泡按钮
        bubble_btn = Button(
            text='显示气泡',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.8, 0.8, 0.4, 1)
        )
        bubble_btn.bind(on_press=self.show_bubble)
        control_layout.add_widget(bubble_btn)
        
        # 返回主页按钮
        back_btn = Button(
            text='返回主页',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.5, 0.5, 0.5, 1)
        )
        back_btn.bind(on_press=partial(self.switch_screen, 'main'))
        control_layout.add_widget(back_btn)
        
        control_tab.add_widget(control_layout)
        tab_panel.add_widget(control_tab)
        
        screen.add_widget(tab_panel)
        return screen
    
    # 事件处理方法
    def switch_screen(self, screen_name, instance):
        """切换屏幕"""
        self.root.current = screen_name
    
    def show_popup(self, message, instance):
        """显示简单弹窗"""
        popup = Popup(
            title='提示',
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        )
        popup.open()
    
    def show_custom_popup(self, instance):
        """显示自定义弹窗"""
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        content.add_widget(Label(text='这是一个自定义弹窗'))
        content.add_widget(TextInput(text='可以在这里输入内容', multiline=False))
        
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50))
        
        ok_btn = Button(text='确定', background_color=(0.2, 0.8, 0.2, 1))
        cancel_btn = Button(text='取消', background_color=(0.8, 0.2, 0.2, 1))
        
        btn_layout.add_widget(ok_btn)
        btn_layout.add_widget(cancel_btn)
        content.add_widget(btn_layout)
        
        popup = Popup(
            title='自定义弹窗',
            content=content,
            size_hint=(0.9, 0.6)
        )
        
        ok_btn.bind(on_press=popup.dismiss)
        cancel_btn.bind(on_press=popup.dismiss)
        
        popup.open()
    
    def show_modal_view(self, instance):
        """显示模态视图"""
        modal = ModalView(size_hint=(0.8, 0.6))
        
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        content.add_widget(Label(text='这是一个模态视图\n点击外部区域关闭', font_size='18sp'))
        
        close_btn = Button(
            text='关闭',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.8, 0.2, 0.2, 1)
        )
        close_btn.bind(on_press=modal.dismiss)
        content.add_widget(close_btn)
        
        modal.add_widget(content)
        modal.open()
    
    def show_bubble(self, instance):
        """显示气泡"""
        bubble = Bubble(
            size_hint=(None, None),
            size=(dp(200), dp(100)),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        
        bubble.add_widget(BubbleButton(text='选项1'))
        bubble.add_widget(BubbleButton(text='选项2'))
        bubble.add_widget(BubbleButton(text='选项3'))
        
        self.root.current_screen.add_widget(bubble)
        
        # 3秒后自动移除气泡
        Clock.schedule_once(lambda dt: self.root.current_screen.remove_widget(bubble), 3)
    
    def update_progress(self, dt):
        """更新进度条"""
        if hasattr(self, 'progress_bar'):
            self.progress_bar.value += 1
            if self.progress_bar.value >= 100:
                self.progress_bar.value = 0
    
    def on_slider_value(self, instance, value):
        """滑块值变化"""
        if hasattr(self, 'slider_value_label'):
            self.slider_value_label.text = f'值: {int(value)}'
    
    def on_checkbox_active(self, instance, value):
        """复选框状态变化"""
        if hasattr(self, 'checkbox_label'):
            self.checkbox_label.text = '已选中' if value else '未选中'
    
    def on_switch_active(self, instance, value):
        """开关状态变化"""
        if hasattr(self, 'switch_label'):
            self.switch_label.text = '开启' if value else '关闭'
    
    def on_spinner_select(self, instance, text):
        """下拉选择器选择"""
        if hasattr(self, 'spinner_result'):
            self.spinner_result.text = f'选择了: {text}'
    
    def on_color_change(self, instance, color):
        """颜色变化"""
        if hasattr(self, 'color_result'):
            r, g, b, a = color
            self.color_result.text = f'选择的颜色: RGB({r:.2f}, {g:.2f}, {b:.2f})'
    
    def on_file_select(self, instance, selection):
        """文件选择"""
        if hasattr(self, 'file_result'):
            if selection:
                filename = selection[0].split('\\')[-1] if '\\' in selection[0] else selection[0].split('/')[-1]
                self.file_result.text = f'选择的文件: {filename}'
            else:
                self.file_result.text = '未选择文件'
    
    def on_start(self):
        try:
            Logger.info("KivyUIDemo: 应用启动完成")
        except Exception as e:
            Logger.error(f"KivyUIDemo: 启动时发生错误: {str(e)}")
    
    def on_stop(self):
        try:
            Logger.info("KivyUIDemo: 应用正在停止")
        except Exception as e:
            Logger.error(f"KivyUIDemo: 停止时发生错误: {str(e)}")

if __name__ == "__main__":
    try:
        Logger.info("主程序: 开始启动Kivy UI演示应用")
        app = KivyUIDemo()
        app.run()
        Logger.info("主程序: 应用正常退出")
    except Exception as e:
        Logger.error(f"主程序: 发生未捕获的异常: {str(e)}")
        Logger.error(f"主程序: 异常详情: {traceback.format_exc()}")
        print(f"应用崩溃: {str(e)}")
        print(f"详细错误信息: {traceback.format_exc()}")
