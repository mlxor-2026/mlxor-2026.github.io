#!/usr/bin/env python3
"""
연사/오거나이저 사진을 내려받아 정사각형으로 리사이즈하여
static/imgs/<slug>.jpg 로 저장합니다 (로드 지연 방지용 경량화).

사용법:
  1) tools/photos.tsv 의 source_image_url 칸에 각 인물의 직접 이미지 URL을 채웁니다.
     (homepage 칸은 사진을 어디서 찾을지에 대한 힌트입니다)
  2) pip install requests pillow
  3) python tools/fetch_photos.py
네트워크가 열린 로컬 환경에서 실행하세요. (대학 사이트 접근 필요)
"""
import csv, os, sys, io
try:
    import requests
    from PIL import Image
except ImportError:
    sys.exit("먼저 설치하세요:  pip install requests pillow")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(ROOT, "tools", "photos.tsv")
OUT = os.path.join(ROOT, "static", "imgs")
SIZE = 320  # 출력 정사각형 한 변(px). 원형으로 표시되므로 정사각형이면 충분.

def cover_square(im, size):
    im = im.convert("RGB")
    w, h = im.size
    s = min(w, h)
    im = im.crop(((w - s)//2, (h - s)//2, (w + s)//2, (h + s)//2))
    return im.resize((size, size), Image.LANCZOS)

def main():
    done, skipped = 0, 0
    with open(TSV, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.lstrip().startswith("#"):
                continue
            cols = line.split("\t")
            if len(cols) < 5 or not cols[4].strip():
                skipped += 1
                print(f"  (건너뜀) {cols[0] if cols else '?'}: 이미지 URL 없음")
                continue
            slug, name, url = cols[0].strip(), cols[1].strip(), cols[4].strip()
            try:
                r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
                r.raise_for_status()
                im = cover_square(Image.open(io.BytesIO(r.content)), SIZE)
                path = os.path.join(OUT, slug + ".jpg")
                im.save(path, "JPEG", quality=85, optimize=True)
                kb = os.path.getsize(path)//1024
                print(f"  OK  {name:24s} -> imgs/{slug}.jpg ({kb} KB)")
                done += 1
            except Exception as e:
                print(f"  실패 {name}: {e}")
    print(f"\n완료: {done}개 저장, {skipped}개 건너뜀")

if __name__ == "__main__":
    main()
