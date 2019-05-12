## 常见的歌词文件

**lrc** 这种歌词文件是一种通用的歌词文件，适用于所有音乐播放器，歌词播放时间精确到行，可以设置每行歌词开始播放的时间，内容可以明文显示

**krc** 这是酷狗音乐专门开发的一种歌词文件，特点是可以将歌词播放时间精确到字，可以设置内行歌词开始时间，持续持续时间，每个字的持续时间等，但是，这是酷狗音乐的一项专利技术，所以对文件进行了转码加密

**qrc**这是腾讯开发的种歌词文件，特点类似于krc，但是文件也可以明文显示

qrc因为明文显示，很容易与lrc转换，本代码适用于krc转换为lrc

## 核心方法
``` python
def decode_krc(krc_name):
　　#接收:krc文件路径 Str类型
　　#返回:标准lrc文本  Str类型
　　......
```
## 使用function
可以自行编写脚本，只需要导入decode_krc()方法

## 使用脚本
可以通过简单修改krc to lrc直接使用脚本，只需要修改music_dir,krc_dir参数即可
### 参数解释
**music_dir**:歌曲所在的文件夹路径，用于获取歌曲列表，会自动去除所有.mp3以外文件
**krc_dir**:krc文件所在文件夹路径，用于获取krc文件列表，自动去除所有.krc以外文件
**工作机制**:获取歌曲列表，获取歌词列表，对比列表后，得到有歌曲存在的歌词文件，调用decode_krc方法得到转码后的歌词内容，生成与歌曲同名的lrc文件，存入歌曲所在目录


