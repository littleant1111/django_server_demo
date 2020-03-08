#!/usr/bin/python
# coding:utf-8
from django.http import JsonResponse

def nav_list(request):
    ret = [
        {
            "path": '/app',
            "name": '首页'
        },
        {
            "name": '系统组件',
            "child": [
                {
                    "name": '介绍',
                    "path": '/app'
                },
                {
                    "name": '功能类',
                    "child": [
                        {
                            "path": '/example/testpagea',
                            "name": '测试页面A'
                        },
                        {
                            "path": '/example/testpageb',
                            "name": '测试页面B'
                        },
                        {
                            "path": '/example/testpagec',
                            "name": '测试页面C'
                        }
                    ]
                },
                {
                    "name": '布局类',
                    "child": [
                        {
                            "path": '/test2/testpagea2',
                            "name": '页面标题'
                        },
                        {
                            "path": '/test2/testpageb2',
                            "name": '子区域'
                        },
                        {
                            "path": '/test2/testpagec2',
                            "name": '搜索条'
                        },
                    ]
                },
                # {
                #     "name": '辅助类',
                #     "child": [
                #         {
                #             "path": '/components/pageNotes',
                #             "name": '引用说明'
                #         }
                #     ]
                # }
            ]
        },
        {
            "name": '完整示例',
            "child": [
                # {
                #     "path": '/example/table',
                #     "name": '列表页面',
                #     "permission": ['edit']
                # },
                # {
                #     "path": '/example/charts',
                #     "name": '图表页面'
                # },
                # {
                #     "path": '/example/map',
                #     "name": '地图页面'
                # }
            ]
        },
        # {
        #     "path": '/i18n',
        #     "name": '国际化'
        # },
        # {
        #     "path": '/theme',
        #     "name": '主题切换'
        # }
        ]

    return JsonResponse(ret, safe=False)

