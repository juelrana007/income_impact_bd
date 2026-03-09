import re
import base64
import zlib
import os

# আপনার ফাইলগুলোর নাম
files = ['ua.py', 'ig.py', 'em.py', 'create.py', 'ig2.py']

for file in files:
    if not os.path.exists(file):
        print(f"ফাইল পাওয়া যায়নি: {file}")
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # রেজেক্স দিয়ে base64 পেলোড খুঁজে বের করা
    match = re.search(r"b'([^']+)'", content)
    if match:
        b64_data = match.group(1)
        try:
            # Base64 ডিকোড এবং zlib ডিকম্প্রেস করা
            decoded_bytes = zlib.decompress(base64.b64decode(b64_data))
            decoded_text = decoded_bytes.decode('utf-8')
            
            # নতুন ফাইলে সেভ করা
            new_filename = file.replace('.py', '_decoded.py')
            with open(new_filename, 'w', encoding='utf-8') as f:
                f.write(decoded_text)
            print(f"✅ সফলভাবে ডিকোড হয়েছে: {file} -> {new_filename}")
        except Exception as e:
            print(f"❌ ডিকোড করতে সমস্যা হয়েছে {file}: {e}")
    else:
        print(f"⚠️ {file} ফাইলে কোনো পেলোড পাওয়া যায়নি।")
