[app]

# (str) Title of your application
title = MyVoiceTest

# (str) Package name
package.name = voicetest

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
# 🔴 关键修改：指向你的 app 目录
source.dir = app

# (str) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# 🔴 关键修改：添加了 audio 处理需要的库
requirements = python3,kivy==2.2.0,plyer,android

# (list) Permissions
# 🔴 关键修改：申请录音和存储权限
android.permissions = RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 31
android.minapi = 21

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) The format used to package the app for release modes (aab or apk or aar).
android.release_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0