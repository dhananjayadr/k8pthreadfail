import numpy as np
import threading
import time
import os
import sys

def exhaust_threads():
    """Exhaust available threads first"""
    threads = []
    def keep_alive():
        time.sleep(60)
    
    try:
        for i in range(50):
            t = threading.Thread(target=keep_alive)
            t.daemon = True
            t.start()
            threads.append(t)
    except:
        pass
    
    print(f"Exhausted threads, created {len(threads)} threads")
    
    # Now force OpenBLAS to try creating its internal threads
    print("\n=== Forcing OpenBLAS to initialize with exhausted threads ===")
    
    # Multiple numpy operations to force OpenBLAS threading
    for i in range(3):
        try:
            print(f"Attempting numpy operation {i+1}...")
            a = np.random.rand(500, 500)
            b = np.random.rand(500, 500)
            result = np.dot(a, b)
            print(f"Operation {i+1} completed")
        except Exception as e:
            print(f"Operation {i+1} failed: {e}")

if __name__ == "__main__":
    exhaust_threads()
