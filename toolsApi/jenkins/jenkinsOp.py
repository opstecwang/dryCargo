##! /usr/bin/env python3

import jenkins

server = jenkins.Jenkins(url='http://office-jenkins.haihuman.com/', username='admin', password='Niren1qaz!QAZ')

# 列出所有项目
value = []
for i in server.get_all_jobs():
    value.append(i['name'])
print(value)

print(server.get_all_jobs()[1])

help(jenkins.Jenkins)

print(server.assert_job_exists('ops-haiops'))

# 立即构建
server.build_job('ops-haiops', parameters={"branch_name": "master"})

# 获取Jenkins版本
print(server.get_version())

# 获取'ops-haiops'最后一次构建号
print(server.get_job_info('ops-haiops')['lastCompletedBuild']['number'])

# 获取'ops-haiops'第34次构建的结果
print(server.get_build_info('ops-haiops', 34)['result'])
print(server.get_build_console_output('ops-haiops', 34).split('\n')[-2].split(':')[-1].strip())
# job状态应该还包括running，pending状态

# 获取'ops-haiops'第34次构建的控制台输出
print(server.get_build_console_output('ops-haiops', 34))

# 复制job
SUBSYS_LIST = ["oauth2", "tms", "oms"]
for SUBSYS in SUBSYS_LIST:
    server.copy_job("sim-"+SUBSYS, "uat-"+SUBSYS)
    print("uat-"+SUBSYS+"任务创建成功")

