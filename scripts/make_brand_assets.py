"""生成 favicon.ico 与 og.png，视觉与 public/favicon.svg 保持一致。

设计来源：深色圆角方块 + Georgia 斜体 "a"（浅色）。
站点配色：背景 #F5F3EE / 文字 #18181B / 强调 #315CF4。
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(os.path.dirname(HERE), "public")

DARK = (24, 24, 27)       # #18181B
LIGHT = (245, 243, 238)   # #F5F3EE
ACCENT = (49, 92, 244)    # #315CF4
MUTED = (91, 91, 97)      # #5B5B61


def find_font(candidates):
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


GEORGIA_ITALIC = find_font([
    r"C:\Windows\Fonts\georgiaz.ttf",
    r"C:\Windows\Fonts\georgiai.ttf",
    r"C:\Windows\Fonts\Georgia Italic.ttf",
])
GEORGIA = find_font([r"C:\Windows\Fonts\georgia.ttf"])
SANS = find_font([r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\msyhbd.ttc"])
MONO = find_font([r"C:\Windows\Fonts\consola.ttf"])


def rounded_icon(size, radius_ratio=0.28):
    """按 favicon.svg 的比例绘制：rx=18/64，字号 48/64，基线 y=47/64。"""
    scale = 4  # 先超采样再缩小，边缘更干净
    s = size * scale
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * radius_ratio), fill=DARK)

    font_size = int(s * (48 / 64))
    font = ImageFont.truetype(GEORGIA_ITALIC, font_size) if GEORGIA_ITALIC else ImageFont.load_default()
    # 用 anchor="ms" 让文字水平居中、垂直基线对齐到 47/64 处
    d.text((s / 2, s * (47 / 64)), "a", font=font, fill=LIGHT, anchor="ms")

    return img.resize((size, size), Image.LANCZOS)


def build_favicon():
    sizes = [16, 32, 48, 64]
    frames = [rounded_icon(n) for n in sizes]
    out = os.path.join(PUBLIC, "favicon.ico")
    # 最大尺寸作为主图，其余作为多尺寸帧写入
    frames[-1].save(out, format="ICO", sizes=[(n, n) for n in sizes], append_images=frames[:-1])
    print("favicon.ico ->", out, os.path.getsize(out), "bytes")


def build_og():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), LIGHT)
    d = ImageDraw.Draw(img)

    # 左侧强调色竖条
    d.rectangle([0, 0, 10, H], fill=ACCENT)

    # 右下角装饰性轨道圆环，呼应首页 hero-art（限制在画布内，避免被裁切）
    d.ellipse([W - 400, H - 250, W - 120, H + 30], outline=(217, 213, 203), width=2)
    d.ellipse([W - 355, H - 205, W - 165, H - 15], outline=ACCENT, width=2)

    # 顶部：品牌标识 + 站点名
    mark_size = 62
    mark = rounded_icon(mark_size)
    img.paste(mark, (92, 82), mark)

    f_name = ImageFont.truetype(SANS, 40) if SANS else ImageFont.load_default()
    d.text((172, 96), "adand", font=f_name, fill=DARK)

    # eyebrow
    f_eyebrow = ImageFont.truetype(MONO, 22) if MONO else ImageFont.load_default()
    d.text((94, 190), "INDEPENDENT NOTES / 2026", font=f_eyebrow, fill=MUTED)

    # 主标题（两行）：中文用无衬线，强调行单独用强调色
    f_h1 = ImageFont.truetype(SANS, 76) if SANS else ImageFont.load_default()
    d.text((94, 236), "把想法", font=f_h1, fill=DARK)
    d.text((94, 330), "做成作品。", font=f_h1, fill=ACCENT)

    # 底部分隔线 + 描述
    d.line([(94, 470), (W - 94, 470)], fill=(217, 213, 203), width=2)
    f_desc = ImageFont.truetype(SANS, 28) if SANS else ImageFont.load_default()
    d.text((94, 500), "记录 AI Agent、自动化工具与工程实践的个人工作台。", font=f_desc, fill=MUTED)

    f_url = ImageFont.truetype(MONO, 22) if MONO else f_eyebrow
    d.text((94, 550), "weufhsos.github.io", font=f_url, fill=ACCENT)

    out = os.path.join(PUBLIC, "og.png")
    img.save(out, format="PNG", optimize=True)
    print("og.png ->", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    print("fonts:", GEORGIA_ITALIC, SANS, MONO)
    build_favicon()
    build_og()
