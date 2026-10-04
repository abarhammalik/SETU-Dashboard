import subprocess, sys, re
sys.stdout.reconfigure(encoding='utf-8')
cp = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
res = subprocess.run([cp, '--headless=new', '--disable-gpu', '--dump-dom', '--virtual-time-budget=7000', 'http://localhost:8501'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
idx = res.stdout.find('MISSION FLIGHT DECK')
if idx != -1:
    print('FOUND! Context:')
    print(res.stdout[max(0, idx-600):min(len(res.stdout), idx+600)])
