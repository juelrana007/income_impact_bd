import os
import re
import base64
import zlib

files = ['ua.py', 'ig.py', 'em.py', 'create.py', 'ig2.py']

for file in files:
    if not os.path.exists(file):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        code = f.read()
    
    print(f"\n[{file}] ডিকোড করা শুরু হচ্ছে...")
    
    layer = 1
    while True:
        # base64 পেলোড খুঁজছি
        match = re.search(r"b'([^']+)'", code)
        if not match:
            break
            
        b64_data = match.group(1)
        try:
            # ডিকোড এবং ডিকম্প্রেস
            decoded_bytes = zlib.decompress(base64.b64decode(b64_data))
            code = decoded_bytes.decode('utf-8')
            print(f" -> লেয়ার {layer} ডিকোড সফল!")
            layer += 1
        except Exception as e:
            print(f" -> ডিকোড করতে সমস্যা: {e}")
            break
            
    # ফাইনাল আউটপুট সেভ করা
    out_filename = file.replace('.py', '_final.py')
    with open(out_filename, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"✅ ফাইনাল ডিকোড সম্পন্ন: {out_filename}")
