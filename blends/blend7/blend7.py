import pandas as pd
import numpy as np
from scipy.stats import spearmanr
from sklearn.metrics import matthews_corrcoef, ConfusionMatrixDisplay
from alaska2.submissions import blend_predictions_ranked, blend_predictions_mean
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix

v25_xl_NR_moreTTA_b4mish = pd.read_csv("submission_v25_xl_NR_moreTTA_b4mish.csv").sort_values(by="Id").reset_index()
submission_v25_xl_NR_moreTTA_b4mish_b2mish_xlmish = (
    pd.read_csv("submission_v25_xl_NR_moreTTA_b4mish_b2mish_xlmish.csv").sort_values(by="Id").reset_index()
)
submission_v26_dctr_jrm_srnet_mns_mnxlm_b2_b4m_b5m_srnetnopc70 = (
    pd.read_csv("submission_v26_dctr_jrm_srnet_mns_mnxlm_b2_b4m_b5m_srnetnopc70.csv")
    .sort_values(by="Id")
    .reset_index()
)

xgb_cls_gs_09445 = pd.read_csv(
    "xgb_cls_gs_0.9445_Cf2cauc_Df1cauc_Ff0cauc_Gf0cauc_Gf1cauc_Gf2cauc_Gf3cauc_Hnrmishf2cauc_.csv"
)

# Force 1.01 value of OOR values in my submission
oor_mask = v25_xl_NR_moreTTA_b4mish.Label > 1.0

xgb_cls_gs_09445.loc[oor_mask, "Label"] = 1.01

submissions = [
    v25_xl_NR_moreTTA_b4mish,
    submission_v25_xl_NR_moreTTA_b4mish_b2mish_xlmish,
    submission_v26_dctr_jrm_srnet_mns_mnxlm_b2_b4m_b5m_srnetnopc70,
    xgb_cls_gs_09445,
]

cm = np.zeros((len(submissions), len(submissions)))
for i in range(len(submissions)):
    for j in range(len(submissions)):
        cm[i, j] = spearmanr(submissions[i].Label, submissions[j].Label).correlation

print(cm)

# disp = ConfusionMatrixDisplay(
#     confusion_matrix=cm,
#     display_labels=["v25_xl_NR_moreTTA", "v25_xl_NR_moreTTA_b4mish", "mean_09406", "xgb_cls_gs_09445"],
# )
# plt.figure(figsize=(8, 8))
# disp.plot(include_values=True, cmap="Blues", ax=plt.gca(), xticks_rotation=45)
# plt.show()

# 939
blend_6_ranked = blend_predictions_ranked([submission_v25_xl_NR_moreTTA_b4mish_b2mish_xlmish, xgb_cls_gs_09445])
blend_6_ranked.to_csv("blend_7_ranked_v25_xl_NR_moreTTA_b4mish_b2mish_xlmish_with_xgb_cls_gs_09445.csv", index=False)

#
blend_6_ranked = blend_predictions_ranked([v25_xl_NR_moreTTA_b4mish, xgb_cls_gs_09445])
blend_6_ranked.to_csv("blend_7_ranked_v25_xl_NR_moreTTA_b4mish_with_xgb_cls_gs_09445.csv", index=False)

blend_6_ranked = blend_predictions_ranked([v25_xl_NR_moreTTA_b4mish, xgb_cls_gs_09445])
blend_6_ranked.to_csv("blend_7_ranked_v26_v26_dctr_jrm_srnet_mns_mnxlm_b2_b4m_b5m_srnetnopc70_with_xgb_cls_gs_09445.csv", index=False)
