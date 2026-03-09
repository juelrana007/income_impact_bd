import os

# আপনার ফাইলগুলোর নাম
files = ['ua.py', 'ig.py', 'em.py', 'create.py', 'ig2.py']

for file in files:
    if not os.path.exists(file):
        print(f"ফাইল পাওয়া যায়নি: {file}")
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        code = f.read()
        
    # কোডের ভেতরের exec কে print এ পরিবর্তন করা
    if "exec(" in code:
        modified_code = code.replace("exec(", "print(")
        
        # একটি টেম্পোরারি ফাইলে সেভ করে রান করা
        temp_filename = "temp_" + file
        with open(temp_filename, 'w', encoding='utf-8') as f:
            f.write(modified_code)
        
        # আউটপুট নতুন ফাইলে সেভ করা
        out_filename = file.replace('.py', '_decoded.py')
        os.system(f"python {temp_filename} > {out_filename}")
        
        # টেম্প ফাইল মুছে ফেলা
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
            
        print(f"✅ সফলভাবে ডিকোড হয়েছে: {file} -> {out_filename}")
    else:
        print(f"⚠️ {file} ফাইলে exec() পাওয়া যায়নি।")
