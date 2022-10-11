# 10、视频水印
# 使用此自动化脚本为你的视频添加水印，该脚本使用 Moviepy，这是一个方便的视频编辑模块。 在下面的脚本中，你可以看到如何添加水印并且可以自由使用它。

# Video Watermark with Python
# pip install moviepy

from moviepy.editor import *
clip = VideoFileClip("myvideo.mp4", audio=True)
width,height = clip.size
text = TextClip("WaterMark", font='Arial', color='white', fontsize=28)
set_color = text.on_color(size=(clip.w + text.w, text.h-10), color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
set_textPos = set_color.set_pos( lambda pos: (max(width/30,int(width-0.5* width* pos)),max(5*height/6,int(100* pos))) )
Output = CompositeVideoClip([clip, set_textPos])
Output.duration = clip.duration
Output.write_videofile("output.mp4", fps=30, codec='libx264')