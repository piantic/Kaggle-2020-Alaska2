import os
import pandas as pd
import torch
from pytorch_toolbelt.utils import logit
from typing import List

output_dir = os.path.dirname(__file__)


def temperature_scaling(x, t):
    x = torch.tensor(x)
    x_l = logit(x)
    x_s = torch.sigmoid(x_l * t)
    return float(x_s)


def sigmoid(x):
    return torch.sigmoid(torch.tensor(x)).item()


def classifier_probas(x):
    x = x.replace("[", "").replace("]", "").split(",")
    x = [float(i) for i in x]
    x = torch.tensor(x).softmax(dim=0)
    x = x[1:].sum()
    return float(x)


def stringify_image_id(x):
    return f"{x:0>4}.jpg"


def submit_from_average_binary(preds: List[str]):
    preds_df = [pd.read_csv(x) for x in preds]

    submission = preds_df[0].copy().rename(columns={"image_id": "Id"})[["Id"]]
    submission["Id"] = submission["Id"].apply(stringify_image_id)
    submission["Label"] = sum([df["pred_modification_flag"].apply(sigmoid).values for df in preds_df]) / len(preds_df)
    return submission


def submit_from_average_classifier(preds: List[str]):
    preds_df = [pd.read_csv(x) for x in preds]

    submission = preds_df[0].copy().rename(columns={"image_id": "Id"})[["Id"]]
    submission["Id"] = submission["Id"].apply(stringify_image_id)
    submission["Label"] = sum([df["pred_modification_type"].apply(classifier_probas).values for df in preds_df]) / len(
        preds_df
    )
    return submission


fold12_hv = [
    # Fold 1
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May15_17_03_ela_skresnext50_32x4d_fold1_fp16/best_loss_test_predictions_flip_hv_tta.csv",
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May15_17_03_ela_skresnext50_32x4d_fold1_fp16/auc/train.74_test_predictions_flip_hv_tta.csv",
    # Fold 2
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May21_13_28_ela_skresnext50_32x4d_fold2_fp16/checkpoints_auc_classifier/best_test_predictions_flip_hv_tta.csv",
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May21_13_28_ela_skresnext50_32x4d_fold2_fp16/checkpoints/best_test_predictions_flip_hv_tta.csv",
]

sub1 = submit_from_average_classifier(fold12_hv)
print(sub1.head())
sub1.to_csv(os.path.join(output_dir, "ela_skresnext50_32x4d_fold12_best_auc_best_loss_classifier.csv"), index=None)

fold12_d4 = [
    # Fold 1
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May15_17_03_ela_skresnext50_32x4d_fold1_fp16/best_loss_test_predictions_d4_tta.csv",
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May15_17_03_ela_skresnext50_32x4d_fold1_fp16/auc/train.74_test_predictions_d4_tta.csv",
    # Fold 2
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May21_13_28_ela_skresnext50_32x4d_fold2_fp16/checkpoints/best_test_predictions_d4_tta.csv",
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May21_13_28_ela_skresnext50_32x4d_fold2_fp16/checkpoints_auc_classifier/best_test_predictions_d4_tta.csv",
]

sub2 = submit_from_average_classifier(fold12_d4)
print(sub2.head())
sub2.to_csv(os.path.join(output_dir, "ela_skresnext50_32x4d_fold12_d4_best_auc_best_loss_classifier.csv"), index=None)

loss_only_fold12_d4 = [
    # Fold 1
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May15_17_03_ela_skresnext50_32x4d_fold1_fp16/best_loss_test_predictions_d4_tta.csv",
    # "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May15_17_03_ela_skresnext50_32x4d_fold1_fp16/auc/train.74_test_predictions_d4_tta.csv",
    # Fold 2
    "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May21_13_28_ela_skresnext50_32x4d_fold2_fp16/checkpoints/best_test_predictions_d4_tta.csv",
    # "D:/Develop/Kaggle/Kaggle-2020-Alaska2/models/May21_13_28_ela_skresnext50_32x4d_fold2_fp16/checkpoints_auc_classifier/best_test_predictions_d4_tta.csv",
]

sub3 = submit_from_average_classifier(loss_only_fold12_d4)
print(sub3.head())
sub3.to_csv(os.path.join(output_dir, "ela_skresnext50_32x4d_fold12_d4_best_loss_classifier.csv"), index=None)
