#!/bin/bash

./SR 10 0 0 10 2 &> log1
./SR 20 0.1 0 10 2 &> log2
./SR 20 0 0.1 10 2 &> log3
./SR 20 0.1 0.1 10 2 &> log4

