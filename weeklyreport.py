import json
import codecs
import io
from pybacklogpy.BacklogConfigure import BacklogJpConfigure
from pybacklogpy.Issue import Issue
from pybacklogpy.Project import Project
from datetime import datetime, date, timedelta

def getCountData(content):
    jsonData = json.loads(content.text)
    return jsonData["count"]
    

config = BacklogJpConfigure(space_key='XXXX',
                             api_key='XXXX')

dicProject = {
    "projectCode"   : project_id,
    "projectCode"   : project_id,
    "projectCode"   : project_id,
    "projectCode"   : project_id,
    "projectCode"   : project_id
}

issue_api = Issue(config)  

dicTotalCount = { 
    "1" : 0,    # 未着手
    "2" : 0,    # 処理中
    "3" : 0,    # 処理終了
    "4" : 0     # クローズ
}

dicProjectCount = dicTotalCount

dicNewClose= { 
    "new" : 0,
    "close": 0
}

untilDay = datetime.today().strftime('%Y-%m-%d')
sinceDay = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

for  proKey , proValue in dicProject.items():
    countNewIssue = issue_api.count_issue(project_id=proValue, created_since=sinceDay , created_until=untilDay)
    countCloseIssue = issue_api.count_issue(project_id=proValue, status_id=4, updated_since=sinceDay , updated_until=untilDay)
    dicNewClose["new"] += getCountData(countNewIssue)
    dicNewClose["close"] += getCountData(countCloseIssue)

    for i in range(1,5):
        countJson = issue_api.count_issue(project_id=proValue,status_id=i)
        dicTotalCount[str(i)] += getCountData(countJson)
        dicProjectCount[str(i)] = getCountData(countJson) 
        
    print(proKey)
    print(dicProjectCount)

print("新規")
print(dicNewClose)
print("合計")
print(dicTotalCount)


