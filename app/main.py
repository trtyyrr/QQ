from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
from plyer import audio
import os

# 界面布局 (KV)
KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 50
    spacing: 30
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    
    Label:
        id: status_label
        text: '等待指令...'
        font_size: '24sp'
        color: 1, 1, 1, 1
        halign: 'center'
    
    Button:
        id: record_btn
        text: '按住录音 / 点击停止'
        font_size: '22sp'
        background_color: 0, 0.6, 0.8, 1
        on_release: app.toggle_recording()
'''

class VoiceApp(App):
    def build(self):
        return Builder.load_string(KV)

    def toggle_recording(self):
        # 1. 动态申请安卓权限 (核心步骤)
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.RECORD_AUDIO, Permission.WRITE_EXTERNAL_STORAGE])
        
        btn = self.root.ids.record_btn
        lbl = self.root.ids.status_label
        
        # 2. 录音逻辑
        try:
            # 文件会保存在 App 的私有目录或 SD 卡
            file_path = 'test_voice.3gp'
            
            if "停止" not in btn.text:
                # 开始录音
                audio.start()
                lbl.text = "🎙️ 正在录音...\n(请大声说话)"
                btn.text = "⏹️ 停止录音"
                btn.background_color = (0.9, 0.1, 0.1, 1) # 变红
            else:
                # 停止录音
                audio.stop()
                lbl.text = "✅ 录音完成"
                btn.text = "再次录音"
                btn.background_color = (0, 0.6, 0.8, 1) # 变蓝
                
        except Exception as e:
            lbl.text = f"出错: {str(e)}"

if __name__ == '__main__':
    VoiceApp().run()