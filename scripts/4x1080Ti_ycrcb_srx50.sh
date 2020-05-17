export KAGGLE_2020_ALASKA2=/home/bloodaxe/datasets/ALASKA2

python train.py -m ycrcb_skresnext50_32x4d -b 80 -w 16 -d 0.2 -s flat_cos -o Ranger --epochs 75 -a light\
  --modification-flag-loss bce 1 --modification-type-loss ce 0.1 -lr 1e-3 --fold 0 --seed 0 --fp16\
  --transfer /home/bloodaxe/develop/Kaggle-2020-Alaska2/runs/May13_23_00_rgb_skresnext50_32x4d_fold0_fp16/main/checkpoints_auc/best.pth

