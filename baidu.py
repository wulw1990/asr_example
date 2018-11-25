"""百度语音识别接口调用示例

准备工作：

安装baidu的python sdk:
pip install baidu-aip

注册自己的APP ID:
 1) 登录: https://console.bce.baidu.com/ai/?fromai=1#/ai/speech/overview/index
 2) 创建应用
 3) 获取 APP_ID API_KEY SECRET_KEY等信息，填入脚本的对应位置

安装ffmpeg(windows):
 1) 下载: https://ffmpeg.zeranoe.com/builds/
 2) 解压：放到一个固定的路径，例如：C:\software\ffmpeg\
 3) 设置环境变量：将其中的bin路劲（C:\software\ffmpeg\bin）加入到系统路径，
    右键单击“我的电脑”或“此电脑” -> 高级系统设置 -> 环境变量 -> Path -> 
    编辑 -> 新建 -> 填入上述路径 -> 确定
 4) 验证：重新打开一个cmd窗口，输入ffmpeg，有一堆ffmpeg信息，说明安装正确。

安装ffmpeg(linux):
  git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg
  cd ffmpeg
  ./configure --prefix=/opt/ffmpeg --enable-pthreads --enable-shared --enable-gpl --disable-x86asm
  make -j 8
  sudo make install
  export PATH=/opt/ffmpeg/bin:$PATH # ~/.bashrc
  export LD_LIBRARY_PATH=/opt/ffmpeg/lib:$LD_LIBRARY_PATH # ~/.bashrc

准备音频:
 1) 录制音频: 比如可以用手机或者电脑的录音功能
 2) 格式转换: 假设录制的音频文件为hello.w4a, 可以使用如下命令进行格式转换：
    ffmpeg -i hello.m4a -f wav -ar 16000 hello.wav
    得到的hello.wav即可用于调用该语音识别脚本

参考文档：
 http://ai.baidu.com/docs#/ASR-Online-Python-SDK/top
"""
from aip import AipSpeech

APP_ID = '14938451'
API_KEY = 'dvUR73XqvkYi6FuVHWZsVek8'
SECRET_KEY = 'Nwbe8wdnVAlodASKWKSLS0v8ItetIMx7'

audio_file = 'hello.wav'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
result = client.asr(get_file_content(audio_file), 'wav', 16000, {
    'dev_pid': 1536,
})
print(result)
