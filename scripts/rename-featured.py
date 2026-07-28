import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '../content/news'))

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.gif')

def process_post(post_dir):
    # Get all entries in the post directory (non-recursive)
    entries = os.listdir(post_dir)
    
    # Find image files located directly in the post root folder
    root_images = [
        f for f in entries
        if f.lower().endswith(IMAGE_EXTENSIONS) and os.path.isfile(os.path.join(post_dir, f))
    ]

    if not root_images:
        return

    # Skip if 'featured.jpg' already exists
    if 'featured.jpg' in root_images:
        return

    # Pick the first image found
    old_filename = root_images[0]
    old_path = os.path.join(post_dir, old_filename)
    new_path = os.path.join(post_dir, 'featured.jpg')

    os.rename(old_path, new_path)
    
    relative_path = os.path.relpath(post_dir, CONTENT_DIR).replace('\\', '/')
    print(f"✅ Renamed: {relative_path}/{old_filename} ➔ featured.jpg")

if __name__ == '__main__':
    print("🚀 Scanning post folders to rename root images to featured.jpg...")
    for root, dirs, files in os.walk(CONTENT_DIR):
        if any(f.endswith('.md') for f in files):
            process_post(root)