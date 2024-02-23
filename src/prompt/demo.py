import os

from tool import get_completion

# case1
def case1():
    text = f"""
    您应该提供尽可能清晰、具体的指示，以表达您希望模型执行的任务。\
    这将引导模型朝向所需的输出，并降低收到无关或不正确响应的可能性。\
    不要将写清晰的提示词与写简短的提示词混淆。\
    在许多情况下，更长的提示词可以为模型提供更多的清晰度和上下文信息，从而导致更详细和相关的输出。
    """
    # 需要总结的文本内容
    prompt = f"""
    把用三个反引号括起来的文本总结成一句话。
    ```{text}```
    """
    # 指令内容，使用 ``` 来分隔指令和待总结的内容
    response = get_completion(prompt)
    print(response)

def case2():
    prompt = f"""
    请生成包括书名、作者和类别的三本虚构的、非真实存在的中文书籍清单，\
    并以 JSON 格式提供，其中包含以下键:book_id、title、author、genre。
    """
    response = get_completion(prompt)
    print(response)

case2()

