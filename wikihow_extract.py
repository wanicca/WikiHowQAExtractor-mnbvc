#%%
from wikihow_parser import Article
import json

#%%

#scheme
ID = "编号"
Q = "问题"
A = "回答"
A_SUM = "简要回答"
PREV = "前承"
NEXT = "后续"
A_STRUCT = "结构"
METHOD = "方法"
STEP = "步骤"
NUMBER = "编号"
TIPS = "小提示"
WARN = "注意事项"
TITLE = "标题"
DESC = "描述"


def process_page(page):
    article = Article(page)
    title = article.title
    answer_sum = article.intro
    answer_struct = {}
    answer = ""
    answer_struct[METHOD] = []
    #METHOD
    for method in article.methods:
        method_title = method.title.partition(':')[-1] if (':') in method.title else method.title
        method_title = method_title.strip()
        answer += f"{method.number}. {method_title}\n"
        method_struct = {NUMBER:method.number,TITLE:method_title,STEP:[]}
        #STEP
        for step in method.steps:
            answer += f"{method.number}-{step.number}. {step.title}\n"
            description = step.description.replace('\n\n','\n').replace('\t',"")
            answer += f"{description}\n"
            method_struct[STEP].append({NUMBER:step.number,TITLE:step.title.strip(), DESC:description.strip()})
        answer_struct[METHOD].append(method_struct)
    #TIPS
    if article.tips:
        for tip in article.tips:
            answer+=tip.replace("\t","").strip() + '\n'
        method_struct[TIPS] = [tip.replace("\t","").strip()+"\n" for tip in article.tips]
    #WARNINGS
    if article.warnings:
        for warn in article.warnings:
            answer+=warn.replace("\t","").strip() + '\n'
        method_struct[WARN] = [warn.replace("\t","").strip() + '\n' for warn in article.warnings]
    result = {Q:title,A:[{A:answer,A_SUM:answer_sum,A_STRUCT:answer_struct}],}
    return result

# %%
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Parse wikihow page into QA data.")
    parser.add_argument("source_files",type=str, nargs="+",help="source html files")
    parser.add_argument("-o","--output",type=str,default="wikihow.jsonl",help="output file")
    args = parser.parse_args()
    with open(args.output,'w') as of:
        for filepath in args.source_files:
            with open(filepath) as f:
                print(json.dumps(process_page(f.read()),ensure_ascii=False),file=of)
    print("Done")