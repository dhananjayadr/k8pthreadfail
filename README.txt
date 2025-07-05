OpenBLAS pthread Resource Exhaustion Test
=========================================

This test reproduces the OpenBLAS pthread_create failure that occurs when 
containers have limited process/thread resources but OpenBLAS tries to create 
multiple threads based on host system limits.

Files
=====
File                         | Purpose
---------------------------- | ----------------------------------------------------------
Dockerfile                   | Container with OpenBLAS/numpy setup
pthread_test.py              | Python script that triggers OpenBLAS pthread errors

How it works
============
1. The script first exhausts available threads by creating 50 daemon threads
2. Then attempts numpy operations that trigger OpenBLAS thread creation
3. OpenBLAS fails to create internal threads due to resource exhaustion
4. Reproduces the exact "pthread_create failed" error seen in production

Build and Run
=============
1. Build the test container - docker build -t pthread-test .
2. Run with severe resource constraints - docker run --rm --cpus="0.02" --memory="32m" --pids-limit=10 -e OPENBLAS_NUM_THREADS=16 pthread-test
3. Run with normal constraints (no error) - docker run --rm pthread-test

Expected Output
===============
1. With resource constraints, you should see,
  - Thread exhaustion message
  - OpenBLAS pthread_create failures
  - "Resource temporarily unavailable" errors

2. Without constraints,
  - All operations complete successfully

Key Parameters
==============
--cpus="0.02"           # Limit CPU to 0.02 cores
--memory="32m"          # Limit memory to 32MB  
--pids-limit=10         # Limit processes/threads to 10
OPENBLAS_NUM_THREADS=16 # Force OpenBLAS to attempt 16 threads
