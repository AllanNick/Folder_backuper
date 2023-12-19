import json
import os
import shutil
import time

with open('conf.json') as f:
    data = json.load(f)

mode = data[0]['mode']
src = data[0]['src']
dst = data[0]['dst']

freq = data[0]['freq']

log_level = data[0]['log_level']
screen_output = data[0]['screen_buffer']

cwd = os.getcwd()

#create log file:
if not os.path.exists('log'):
    os.mkdir('log')
    with open('log/log.txt', 'w') as f:
        t = time.time()
        f.write('log file spawned @timestamp:%s \n'%(t))
        f.write('log level: %s \n'%(log_level))
        f.write('\n')
        f.write('Autobackuper Mark.I rev_0 \n')
        f.write('[C]2018-Now, Nick Computer all rights reserved.\n')
else:
    with open('log/log.txt', 'a') as f:
        t = time.time()
        f.write('============================ \n')
        f.write('[WARN]process was restarted @timestamp:%s \n'%(t))
        f.write('\n')

logdir = os.path.join(cwd, 'log')

def bkp(mode, src, dst, cwd):
    if mode == 'realtive':
        if dst != '':
            dst = os.path.join(cwd, dst)
        else:
            if os.path.exists(os.path.join(cwd, 'backup')):
                dst = os.path.join(cwd, 'backup')
            else:
                os.mkdir(os.path.join(cwd, 'backup'))
                dst = os.path.join(cwd, 'backup')

        os.chdir(dst)

        ctm = time.time()
        f_time = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(ctm))

        if os.path.exists(os.path.join(dst, f_time)):
            #print('backup folder already exists')
            pass
        else:
            #os.mkdir(f_time)
            #os.chdir(f_time)
            write_log(logdir, 'calling up backup task service...', cwd, f_time)
            try:
                shutil.copytree(src, os.path.join(dst, f_time))
                write_log(logdir, 'succeed backup src folder: %s to %s'%(src, dst), cwd, f_time)
            except:
                write_log(logdir, 'failed backup src folder: %s to %s'%(src, dst), cwd, f_time)
                
    os.chdir(cwd)

def write_log(logdir, msg, cwd, f_time):
    global screen_output
    os.chdir(logdir)
    if msg[:6] == 'failed':
        string = '[ERR]'+f_time + ':' + msg + '\n'
    else:
        string = '[INFO]'+f_time + ':' + msg + '\n'
    
    if screen_output == 'ON':
        print(f_time + ':' + msg)
    with open('log.txt', 'a') as f:
        f.write(string)
    os.chdir(cwd)

def main():
    bkp(mode, src, dst, cwd)

if False:
    print('[C]2018-Now, Nick Computer all rights reserved.')

if os.name == 'nt':
    while True:
        main()
        time.sleep(int(freq))
else:
    print('this program is currently only supported on windows')
    sleep(5)





