import threading
import time
import subprocess
import select

# 쓰레드 함수
def tail_func( file_path, q ):
    f = subprocess.Popen(['tail', '-F', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = select.poll()
    p.register(f.stdout)

    while True:
        if p.poll(1):
            print("[LOG] ==> %s, %s" % (file_path, f.stdout.readline()))
            q.put(( file_path, f.stdout.readline() ))
        time.sleep(1)

# 감시자 초기화
def init_watcher( filename, q ):
    # string 받으려면 두번째, 필수 (추가하지 않으면, 각각의 char 로 인식)
    t = threading.Thread(target=tail_func, args=( filename, q, ))
    t.start()