# coding=utf-8

from multiprocessing import Process
import subprocess
import traceback

def submit(command):

    def worker():
        try:
            # do sth database -- start
            sub = subprocess.call(command, shell = True)
        except Exception as e:
            # do sth report
            traceback.print_exc()
        
        # do sth database -- finish

    p = Process(target = worker)
    p.Start()