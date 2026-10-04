
with open('test_dom.py') as f: pass
import subprocess, re
cp = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
res = subprocess.run([cp, '--headless=new', '--disable-gpu', '--dump-dom', '--virtual-time-budget=10000', 'http://localhost:8501'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
matches = re.findall(r'<button[^>]*tab[^>]*>.*?</button>', res.stdout, re.DOTALL | re.IGNORECASE)
print('Found buttons count:', len(matches))
for m in matches[:6]:
    print('BUTTON:', m)
