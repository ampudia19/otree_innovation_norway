import pandas as pd
from ast import literal_eval

LIST_TYPE_COLUMNS = [
    "app_info_unique", "app_info_findout", "app_info_intl", "app_info_pitch", 
    "app_info_indivs", "app_info_confirm", "app_info_attachments", 
    "app_acc_engagements", "app_con_habilitation"
]

ML_COLS = [
    "case_label", "Saknummer", "ProjectName", "Tekst", "TextSimilarity_lemma", 
    "Utfall", "Næringshovedområde", "Innovasjonsnivånavn", "innvilget_INNO_Virkemiddelkategori"
]

def parse_inputs(round):
    df = pd.read_csv(
        "inputs/data.csv",
        index_col=0,
        converters={x: literal_eval for x in LIST_TYPE_COLUMNS}
    )

    return df.loc[df["round"]==round].to_dict(orient="records")[0]

def parse_ml_outputs(round_label):
    df = pd.read_csv(
        "inputs/ml_outputs.csv",
        usecols=ML_COLS,
        header=0,
        sep=";"
    )

    return (
        df
        .loc[df.case_label==round_label]
        .sort_values(by=["TextSimilarity_lemma"], ascending=False)
        [[col for col in df.columns if col not in ["case_label"]]]
        .apply(tuple, axis=1)
        .tolist()
    )