#!/usr/bin/env bash
export CUDA_VISIBLE_DEVICES=
tensorboard --logdir runs --host 0.0.0.0 --port 8888 --window_title "ALASKA2"