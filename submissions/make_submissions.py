import os

from alaska2.metric import alaska_weighted_auc
from alaska2.submissions import (
    make_classifier_predictions,
    make_binary_predictions,
    blend_predictions_mean,
    as_hv_tta,
    as_d4_tta,
)
from submissions.ela_skresnext50_32x4d import ela_skresnext50_32x4d_best_loss


def evaluate(df):
    p1b = make_binary_predictions(df)
    p1c = make_classifier_predictions(df)
    y_true_holdout = p1c[0]["y_true"]
    print("  binary     ", alaska_weighted_auc(y_true_holdout, blend_predictions_mean(p1b)["Label"]))
    print("  multiclass ", alaska_weighted_auc(y_true_holdout, blend_predictions_mean(p1c)["Label"]))


def main():
    output_dir = os.path.dirname(__file__)

    # if False:
    #     # 0.917
    #     submit_from_average_classifier([rgb_tf_efficientnet_b6_ns_best_auc_c[0]]).to_csv(
    #         os.path.join(output_dir, "May28_13_04_rgb_tf_efficientnet_b6_ns_fold0.csv"), index=False
    #     )
    #
    # if False:
    #     # 0.915
    #     submit_from_classifier_calibrated(
    #         [rgb_tf_efficientnet_b6_ns_best_auc_c[0]], [rgb_tf_efficientnet_b6_ns_best_auc_c_oof[0]]
    #     ).to_csv(os.path.join(output_dir, "May28_13_04_rgb_tf_efficientnet_b6_ns_fold0_calibrated.csv"), index=False)
    #
    # # 0.930
    # if False:
    #     # Take best classifier checkpoints for all models and average them using ranking
    #     predictions = make_classifier_predictions(
    #         ela_skresnext50_32x4d_best_auc_c
    #         + rgb_tf_efficientnet_b6_ns_best_auc_c
    #         + rgb_tf_efficientnet_b2_ns_best_auc_c
    #     )
    #     blend_predictions_ranked(predictions).to_csv(
    #         os.path.join(output_dir, "1xb2_2xb6_4xskrx50_classifier_ranked.csv"), index=False
    #     )
    #
    # # 0.930
    # if False:
    #     # Take best classifier checkpoints for all models and average them using ranking
    #     # HV TTA
    #     predictions = make_classifier_predictions(
    #         as_hv_tta(
    #             ela_skresnext50_32x4d_best_auc_c
    #             + rgb_tf_efficientnet_b6_ns_best_auc_c
    #             + rgb_tf_efficientnet_b2_ns_best_auc_c
    #         )
    #     )
    #     blend_predictions_ranked(predictions).to_csv(
    #         os.path.join(output_dir, "1xb2_2xb6_4xskrx50_hv_tta_classifier_ranked.csv"), index=False
    #     )
    #
    # # 0.929
    # if False:
    #     # Take best classifier checkpoints for all models and average them using ranking
    #     # D4 TTA
    #     predictions = make_classifier_predictions(
    #         as_d4_tta(
    #             ela_skresnext50_32x4d_best_auc_c
    #             + rgb_tf_efficientnet_b6_ns_best_auc_c
    #             + rgb_tf_efficientnet_b2_ns_best_auc_c
    #         )
    #     )
    #     blend_predictions_ranked(predictions).to_csv(
    #         os.path.join(output_dir, "1xb2_2xb6_4xskrx50_d4_tta_classifier_ranked.csv"), index=False
    #     )
    #
    # # 0.931
    # if False:
    #     # Take best classifier checkpoints for all models and average them using ranking
    #     predictions = make_classifier_predictions(
    #         ela_skresnext50_32x4d_best_loss
    #         + rgb_tf_efficientnet_b6_ns_best_loss
    #         + rgb_tf_efficientnet_b2_ns_best_auc_c
    #     )
    #     blend_predictions_ranked(predictions).to_csv(
    #         os.path.join(output_dir, "1xb2_2xb6_4xskrx50_best_loss_classifier_ranked.csv"), index=False
    #     )
    #
    # # 0.930
    # if False:
    #     # Take best classifier checkpoints for all models and average them using ranking
    #     predictions = make_classifier_predictions_calibrated(
    #         ela_skresnext50_32x4d_best_loss
    #         + rgb_tf_efficientnet_b6_ns_best_loss
    #         + rgb_tf_efficientnet_b2_ns_best_auc_c,
    #         ela_skresnext50_32x4d_best_loss_oof
    #         + rgb_tf_efficientnet_b6_ns_best_loss_oof
    #         + rgb_tf_efficientnet_b2_ns_best_auc_c_oof,
    #     )
    #     blend_predictions_ranked(predictions).to_csv(
    #         os.path.join(output_dir, "1xb2_2xb6_4xskrx50_best_loss_classifier_calibrated_ranked.csv"), index=False
    #     )
    #
    # # 0.930
    # if False:
    #     # Take best classifier checkpoints for all models and average them using ranking
    #     predictions = make_classifier_predictions_calibrated(
    #         ela_skresnext50_32x4d_best_loss + rgb_tf_efficientnet_b6_ns_best_loss,
    #         # + rgb_tf_efficientnet_b2_ns_best_auc_c,
    #         ela_skresnext50_32x4d_best_loss_oof + rgb_tf_efficientnet_b6_ns_best_loss_oof
    #         # + rgb_tf_efficientnet_b2_ns_best_auc_c_oof,
    #     )
    #     blend_predictions_ranked(predictions).to_csv(
    #         os.path.join(output_dir, "2xb6_4xskrx50_best_loss_classifier_calibrated_ranked.csv"), index=False
    #     )
    #
    # # 0.930
    # if False:
    #     # Take best classifier checkpoints for all models and average them using ranking
    #     predictions = make_classifier_predictions_calibrated(
    #         ela_skresnext50_32x4d_best_loss
    #         + ela_skresnext50_32x4d_best_auc_b
    #         + ela_skresnext50_32x4d_best_auc_c
    #         + rgb_tf_efficientnet_b6_ns_best_loss
    #         + rgb_tf_efficientnet_b6_ns_best_auc_b
    #         + rgb_tf_efficientnet_b6_ns_best_auc_c
    #         + rgb_tf_efficientnet_b2_ns_best_auc_c,
    #         ela_skresnext50_32x4d_best_loss_oof
    #         + ela_skresnext50_32x4d_best_auc_b_oof
    #         + ela_skresnext50_32x4d_best_auc_c_oof
    #         + rgb_tf_efficientnet_b6_ns_best_loss_oof
    #         + rgb_tf_efficientnet_b6_ns_best_auc_b_oof
    #         + rgb_tf_efficientnet_b6_ns_best_auc_c_oof
    #         + rgb_tf_efficientnet_b2_ns_best_auc_c_oof,
    #     )
    #     blend_predictions_ranked(predictions).to_csv(
    #         os.path.join(output_dir, "1xb2_2xb6_4xskrx50_best_lcb_classifier_calibrated_ranked.csv"), index=False
    #     )
    #
    # if False:
    #     # Fold 0
    #     predictions = (
    #         make_classifier_predictions([rgb_tf_efficientnet_b6_ns_best_auc_b[0]])
    #         + make_classifier_predictions_calibrated(
    #             as_d4_tta([ela_skresnext50_32x4d_best_loss[1]]), as_d4_tta([ela_skresnext50_32x4d_best_loss_oof[1]])
    #         )
    #         + make_binary_predictions_calibrated(
    #             [ela_skresnext50_32x4d_best_loss[2]], [ela_skresnext50_32x4d_best_loss_oof[2]]
    #         )
    #         + make_classifier_predictions_calibrated(
    #             [ela_skresnext50_32x4d_best_auc_b[3]], [ela_skresnext50_32x4d_best_auc_b_oof[3]]
    #         )
    #     )
    #
    #     # 0.931
    #     blend_predictions_ranked(predictions).to_csv(
    #         os.path.join(output_dir, "best_models_for_each_fold_ranked.csv"), index=False
    #     )
    #
    #     # 0.929
    #     blend_predictions_mean(predictions).to_csv(
    #         os.path.join(output_dir, "best_models_for_each_fold_mean.csv"), index=False
    #     )
    #
    # if False:
    #     p1 = blend_predictions_mean(make_classifier_predictions(rgb_tf_efficientnet_b6_ns_best_auc_c))
    #     p2 = blend_predictions_mean(make_classifier_predictions(rgb_tf_efficientnet_b6_ns_best_loss))
    #     p3 = blend_predictions_mean(make_classifier_predictions(ela_skresnext50_32x4d_best_loss))
    #     p4 = blend_predictions_mean(make_classifier_predictions(rgb_tf_efficientnet_b2_ns_best_auc_c))
    #
    #     blend_predictions_ranked([p1, p2, p3, p4]).to_csv(
    #         os.path.join(output_dir, "averaged_folds_ensemble_ranked.csv"), index=False
    #     )
    #
    # if False:
    #     best_loss = [
    #         "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints/best_test_predictions.csv"
    #     ]
    #     best_bauc = [
    #         "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc/best_test_predictions.csv"
    #     ]
    #     best_cauc = [
    #         "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc_classifier/best_test_predictions.csv"
    #     ]
    #
    #     best_loss_oof = [
    #         "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints/best_oof_predictions.csv"
    #     ]
    #     best_bauc_oof = [
    #         "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc/best_oof_predictions.csv"
    #     ]
    #     best_cauc_oof = [
    #         "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc_classifier/best_oof_predictions.csv"
    #     ]
    #
    #     best_loss_h = [
    #         "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints/best_holdout_predictions.csv"
    #     ]
    #     best_bauc_h = [
    #         "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc/best_holdout_predictions.csv"
    #     ]
    #     best_cauc_h = [
    #         "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc_classifier/best_holdout_predictions.csv"
    #     ]
    #
    #     for p in best_loss_h + best_bauc_h + best_cauc_h + best_loss_oof + best_bauc_oof + best_cauc_oof:
    #         print(p)
    #         p = pd.read_csv(p)
    #         print(
    #             alaska_weighted_auc(p["true_modification_flag"], p["pred_modification_type"].apply(classifier_probas))
    #         )
    #
    #     blend_predictions_mean(make_classifier_predictions(best_loss + best_cauc)).to_csv(
    #         os.path.join(output_dir, "Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_best_loss_cauc.csv"), index=False
    #     )
    #
    #     p1 = make_classifier_predictions(best_loss_h)[0]
    #     p2 = make_classifier_predictions(best_bauc_h)[0]
    #     p3 = make_classifier_predictions(best_cauc_h)[0]
    #     #
    #     y_true_holdout = p1["y_true"]
    #     p_ranked = blend_predictions_ranked([p1, p2, p3])
    #     p_mean = blend_predictions_mean([p1, p2, p3])
    #     print("Ranked", alaska_weighted_auc(y_true_holdout, p_ranked["Label"]))
    #     print("Averaged", alaska_weighted_auc(y_true_holdout, p_mean["Label"]))
    #
    #     #
    #     p1 = make_classifier_predictions_calibrated(best_loss_h, best_loss_oof)[0]
    #     p2 = make_classifier_predictions_calibrated(best_bauc_h, best_bauc_oof)[0]
    #     p3 = make_classifier_predictions_calibrated(best_cauc_h, best_cauc_oof)[0]
    #     #
    #     y_true_holdout = p1["y_true"]
    #     p_ranked = blend_predictions_ranked([p1, p2, p3])
    #     p_mean = blend_predictions_mean([p1, p2, p3])
    #     print("Ranked Calibrated", alaska_weighted_auc(y_true_holdout, p_ranked["Label"]))
    #     print("Averaged Calibrated", alaska_weighted_auc(y_true_holdout, p_mean["Label"]))
    #
    #     #
    #     p1 = make_classifier_predictions_calibrated(best_loss, best_loss_oof)[0]
    #     p1.to_csv(
    #         os.path.join(
    #             output_dir, "Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16_best_loss_calibrated.csv"
    #         ),
    #         index=False,
    #     )
    #
    #     p2 = make_classifier_predictions_calibrated(best_bauc, best_bauc_oof)[0]
    #     p2.to_csv(
    #         os.path.join(
    #             output_dir, "Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16_best_bauc_calibrated.csv"
    #         ),
    #         index=False,
    #     )
    #
    #     p3 = make_classifier_predictions_calibrated(best_cauc, best_cauc_oof)[0]
    #     p3.to_csv(
    #         os.path.join(
    #             output_dir, "Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16_best_cauc_calibrated.csv"
    #         ),
    #         index=False,
    #     )
    #
    #     p_mean = blend_predictions_mean([p1, p2, p3])
    #     p_mean[["Id", "Label"]].to_csv(
    #         os.path.join(
    #             output_dir, "Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16_best_3_calibrated_mean.csv"
    #         ),
    #         index=False,
    #     )

    if True:
        best_loss = [
            "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints/best_test_predictions.csv",
            "models/Jun09_16_38_rgb_tf_efficientnet_b6_ns_fold1_local_rank_0_fp16/main/checkpoints/best_test_predictions.csv",
            "models/Jun11_08_51_rgb_tf_efficientnet_b6_ns_fold2_local_rank_0_fp16/main/checkpoints/best_test_predictions.csv",
            "models/Jun11_18_38_rgb_tf_efficientnet_b6_ns_fold3_local_rank_0_fp16/main/checkpoints/best_test_predictions.csv",
        ]
        best_bauc = [
            "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc/best_test_predictions.csv",
            "models/Jun09_16_38_rgb_tf_efficientnet_b6_ns_fold1_local_rank_0_fp16/main/checkpoints_auc/best_test_predictions.csv",
            "models/Jun11_08_51_rgb_tf_efficientnet_b6_ns_fold2_local_rank_0_fp16/main/checkpoints_auc/best_test_predictions.csv",
            "models/Jun11_18_38_rgb_tf_efficientnet_b6_ns_fold3_local_rank_0_fp16/main/checkpoints_auc/best_test_predictions.csv",
        ]
        best_cauc = [
            "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc_classifier/best_test_predictions.csv",
            "models/Jun09_16_38_rgb_tf_efficientnet_b6_ns_fold1_local_rank_0_fp16/main/checkpoints_auc_classifier/best_test_predictions.csv",
            "models/Jun11_08_51_rgb_tf_efficientnet_b6_ns_fold2_local_rank_0_fp16/main/checkpoints_auc_classifier/best_test_predictions.csv",
            "models/Jun11_18_38_rgb_tf_efficientnet_b6_ns_fold3_local_rank_0_fp16/main/checkpoints_auc_classifier/best_test_predictions.csv",
        ]

        best_loss_h = [
            "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints/best_holdout_predictions.csv",
            "models/Jun09_16_38_rgb_tf_efficientnet_b6_ns_fold1_local_rank_0_fp16/main/checkpoints/best_holdout_predictions.csv",
            "models/Jun11_08_51_rgb_tf_efficientnet_b6_ns_fold2_local_rank_0_fp16/main/checkpoints/best_holdout_predictions.csv",
            "models/Jun11_18_38_rgb_tf_efficientnet_b6_ns_fold3_local_rank_0_fp16/main/checkpoints/best_holdout_predictions.csv",
        ]
        best_bauc_h = [
            "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc/best_holdout_predictions.csv",
            "models/Jun09_16_38_rgb_tf_efficientnet_b6_ns_fold1_local_rank_0_fp16/main/checkpoints_auc/best_holdout_predictions.csv",
            "models/Jun11_08_51_rgb_tf_efficientnet_b6_ns_fold2_local_rank_0_fp16/main/checkpoints_auc/best_holdout_predictions.csv",
            "models/Jun11_18_38_rgb_tf_efficientnet_b6_ns_fold3_local_rank_0_fp16/main/checkpoints_auc/best_holdout_predictions.csv",
        ]
        best_cauc_h = [
            "models/Jun05_08_49_rgb_tf_efficientnet_b6_ns_fold0_local_rank_0_fp16/main/checkpoints_auc_classifier/best_holdout_predictions.csv",
            "models/Jun09_16_38_rgb_tf_efficientnet_b6_ns_fold1_local_rank_0_fp16/main/checkpoints_auc_classifier/best_holdout_predictions.csv",
            "models/Jun11_08_51_rgb_tf_efficientnet_b6_ns_fold2_local_rank_0_fp16/main/checkpoints_auc_classifier/best_holdout_predictions.csv",
            "models/Jun11_18_38_rgb_tf_efficientnet_b6_ns_fold3_local_rank_0_fp16/main/checkpoints_auc_classifier/best_holdout_predictions.csv",
        ]

        # print("OOF")
        # for p in best_loss_oof + best_bauc_oof + best_cauc_oof:
        #     print(p)
        #     p = pd.read_csv(p)
        #     y_true = p["true_modification_flag"]
        #     print(
        #         alaska_weighted_auc(y_true, p["pred_modification_flag"]),
        #         alaska_weighted_auc(y_true, p["pred_modification_type"].apply(classifier_probas)),
        #     )
        #
        # print("Holdout")
        # for p in best_loss_h + best_bauc_h + best_cauc_h:
        #     print(p)
        #     p = pd.read_csv(p)
        #     y_true = p["true_modification_flag"]
        #     print(
        #         alaska_weighted_auc(y_true, p["pred_modification_flag"]),
        #         alaska_weighted_auc(y_true, p["pred_modification_type"].apply(classifier_probas)),
        #     )
        # print("Loss")
        # print("  No TTA")
        # evaluate(best_loss_h)
        # print("  HV TTA")
        # evaluate(as_hv_tta(best_loss_h))
        # print("  D4 TTA")
        # evaluate(as_d4_tta(best_loss_h))
        #
        # print("B-AUC")
        # print("  No TTA")
        # evaluate(best_bauc_h)
        # print("  HV TTA")
        # evaluate(as_hv_tta(best_bauc_h))
        # print("  D4 TTA")
        # evaluate(as_d4_tta(best_bauc_h))
        #
        # print("C-AUC")
        # print("  No TTA")
        # evaluate(best_cauc_h)
        # print("  HV TTA")
        # evaluate(as_hv_tta(best_cauc_h))
        # print("  D4 TTA")
        # evaluate(as_d4_tta(best_cauc_h))

        # Blends
        blend_predictions_mean(make_classifier_predictions(as_d4_tta(best_cauc)))[["Id", "Label"]].to_csv(
            os.path.join(output_dir, "rgb_tf_efficientnet_b6_ns_best_cauc_d4_mean_holdout_9349.csv"), index=False
        )

        blend = blend_predictions_mean(make_classifier_predictions(as_d4_tta(best_cauc)) +
                                       make_classifier_predictions(as_d4_tta(ela_skresnext50_32x4d_best_loss)))

        blend[["Id", "Label"]].to_csv(
            os.path.join(output_dir, "blend_rgb_tf_efficientnet_b6_ns_best_cauc_d4_ela_skresnext50_32x4d_best_loss_mean_holdout_XXXX.csv"), index=False
        )



if __name__ == "__main__":
    main()
