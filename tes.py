"""
节点：收到任务，开始采集，子任务：开始、结束，上传：成功、失败
"""

msg = {
    'hospital_id': '',   # 医院ID
    'case_id': '',
    'task': '',     # 任务
    'status': '',   # 状态
    'error': '',
    'desc': '',     # 描述
    'count': '',
    'ext1': '',     # 备用
    'ext2': ''      # 备用
}

log = {
    "business": "${business}",  # 项目
    "module": "${module}",  # 模块
    "logTime": "%date{'yyyy-MM-dd HH:mm:ss.SSS'}",  # 时间
    "process": "%process",  # 进程
    "thread": "%thread",  # 线程
    "logLevel": "%level",  # 日志级别
    "className": "%class",  # 类名
    "logMsg": {
        '医院ID': '',
        'caseID': '',
        '任务': '',
        '状态': '',
        'error': '',
        '描述': '',
        'count': '',
        '备用1': '',
        '备用2': ''
    },  # 日志文本
    "stackTrace": "%exception"  # 堆栈错误信息
}
