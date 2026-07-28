import os
import json
import re

BASE_REMOTE_URL = 'https://files.groznet.com/patriot95/news/'

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '../content/news'))

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.gif')

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def process_post(post_dir):
    relative_path = os.path.relpath(post_dir, CONTENT_DIR).replace('\\', '/')
    local_images_dir = os.path.join(post_dir, 'images')

    # Skip if there is no local /images/ folder
    if not os.path.isdir(local_images_dir):
        return

    # Find all local image files
    images = [
        f for f in os.listdir(local_images_dir)
        if f.lower().endswith(IMAGE_EXTENSIONS) and os.path.isfile(os.path.join(local_images_dir, f))
    ]

    if images:
        images.sort(key=natural_sort_key)
        remote_images_url = f"{BASE_REMOTE_URL}{relative_path}/images/"

        output = {
            "remote_base_url": remote_images_url,
            "featured_image": f"{BASE_REMOTE_URL}{relative_path}/featured.jpg",
            "images": images
        }

        json_path = os.path.join(post_dir, 'gallery.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=4, ensure_ascii=False)

        print(f"✅ Generated: {relative_path}/gallery.json ({len(images)} images)")

if __name__ == '__main__':
    print("🚀 Scanning local post folders for images...")
    for root, dirs, files in os.walk(CONTENT_DIR):
        if any(f.endswith('.md') for f in files):
            process_post(root)