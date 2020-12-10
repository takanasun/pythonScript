import csv
import glob
import os
import pandas as pd

files = glob.glob("./検索キーワード/*.csv", )

for file in files:
    with open(file, 'r', encoding='shift_jisx0213') as infile, open( './検索キーワード/tmp_' + os.path.basename(file), 'a' , encoding='shift_jisx0213') as outfile:
        # output dict needs a list for new column ordering
        fieldnames = ["column1","column3","column6","column2","column4","column7","column5"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)
    df = pd.read_csv('./検索キーワード/tmp_' + os.path.basename(file) , encoding='shift_jisx0213')
    keep_col=["totteokitai column1","totteokitai column2","totteokitai column4","totteokitai column6"]
    df['検索ワード'] = 'himitsu'
    new_f = df[keep_col]
    new_f.to_csv('./検索キーワード/re/remake_' + os.path.basename(file) , encoding='shift_jisx0213', index=False)