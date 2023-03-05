# coding=utf-8
"""
@author MrLi
@date 2023.03.05
@description 简单聊天测试
"""

import openai

openai.api_key = 'sk-...'
completion = openai.Completion(model='gpt-3.5-turbo', prompt='Hi')
print(completion.choices[0].text)
