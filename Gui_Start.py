import concurrent.futures
import subprocess

# List of Python scripts to run
scripts_to_run = ['D:\\NetAdminPro Client\\main.py', 'D:\\NetAdminPro Client\\ScreenSharingClient.py','D:\\NetAdminPro Client\\ShareFolderClient.py','D:\\NetAdminPro Client\\LogClient.py']
def run_script(script):
    try:
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_script, scripts_to_run)
