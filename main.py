import logging
import traceback
from kivy.app import App
from kivy.uix.label import Label
from kivy.logger import Logger

# 配置日志
logging.basicConfig(level=logging.DEBUG)
Logger.setLevel(logging.DEBUG)

class MyApp(App):
    def build(self):
        try:
            Logger.info("MyApp: 开始构建应用界面")
            label = Label(text="Hello Android from Kivy!")
            Logger.info("MyApp: 应用界面构建成功")
            return label
        except Exception as e:
            Logger.error(f"MyApp: 构建界面时发生错误: {str(e)}")
            Logger.error(f"MyApp: 错误详情: {traceback.format_exc()}")
            return Label(text="应用启动失败，请检查日志")
    
    def on_start(self):
        try:
            Logger.info("MyApp: 应用启动完成")
        except Exception as e:
            Logger.error(f"MyApp: 启动时发生错误: {str(e)}")
    
    def on_stop(self):
        try:
            Logger.info("MyApp: 应用正在停止")
        except Exception as e:
            Logger.error(f"MyApp: 停止时发生错误: {str(e)}")

if __name__ == "__main__":
    try:
        Logger.info("主程序: 开始启动应用")
        app = MyApp()
        app.run()
        Logger.info("主程序: 应用正常退出")
    except Exception as e:
        Logger.error(f"主程序: 发生未捕获的异常: {str(e)}")
        Logger.error(f"主程序: 异常详情: {traceback.format_exc()}")
        print(f"应用崩溃: {str(e)}")
        print(f"详细错误信息: {traceback.format_exc()}")
