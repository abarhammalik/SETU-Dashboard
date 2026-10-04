import subprocess
cp = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
res = subprocess.run([cp, '--headless=new', '--disable-gpu', '--dump-dom', '--virtual-time-budget=8000', 'http://localhost:8501'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
print('DOM length:', len(res.stdout))
for line in res.stdout.splitlines():
    if 'data-baseweb' in line:
        print(line[:140])
