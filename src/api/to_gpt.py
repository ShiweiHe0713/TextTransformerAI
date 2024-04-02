import openai
import requests
import pandas as pd
import openpyxl

def toGPT(text_arr):
    api_endpoint = "https://api.openai.com/v1/chat/completions" 
    key = pd.read_excel("/Users/starrio/Developer/confidentials.xlsx")
    api_key = key['key'].iloc[0]

    prompt = """请帮我提取以下信息：1、姓名（【之前的内容均为姓名）2、官职（取最大官职，保留一个） 3、功名（高频词：状元、榜眼、探花、进士、贡生、举, 如果都不是则为NA） 4、籍贯（可调用GPT自己的知识库提供） 
                5、生活朝代（可调用GPT自己的知识库提供，格式为xxx朝） 6、入志缘由（请根据行内容进行五个字以内概述）7、入志原因（只需要根据所提供语料保留1个数字序号就好，
                具体标准为：1=忠臣；2=良将；3=廉吏；4=政绩；5=儒学；6=书法艺术；7=孝道；8=其他）.
                提取出的信息请以逗号来分隔，返回内容里不能包含栏目名称（比如“功名”）
            """
    processed_text = []
    chunk_size = 1 # Process 15 people at a time
          
    for text_chunk in text_arr:

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": prompt},
                        {"role": "user", "content": text_chunk}],
            "temperature": 0. #温度调节，数量越大，回答越多样，相应模型功耗也越大，一般0.0-0.5即可
        }

        # 发起 API 请求（代码不变）
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

        # 尝试执行 API 请求，如果发生异常，则捕获异常并打印错误信息，然后继续执行下一轮循环。
        try:
            response = requests.post(api_endpoint, json=data, headers=headers)
            response_data = response.json()

            # 解析 API 响应并获取分类结果（代码不变）
            classification_result = response_data["choices"][0]["message"]["content"]
            processed_text.append(classification_result.strip('"'))
        except Exception as e:
            print(f"Error: {e}")
            pass
    return processed_text
    
text = ["汉祢衡【平原人魏建安中刘表送衡与江夏黄祖祖善待之祖长子射尤善衡尝与俱游共读蔡 邕所作碑文射爱其辞还恨不缮写衡曰吾能识之惟其中碑缺二字为不明耳因书出之射驰使写碑 还校如衡所书莫不叹服射时大会宾客有献鹦鹉者射举巵於衡曰愿先生赋之以娱嘉宾衡揽笔而 作文无加点辞令甚丽後黄祖在蒙冲船上大会宾客而衡言不逊顺祖惭乃诃之欲加箠衡大骂祖恚 杀之】",
        "晋高悝【广陵人寓居江州刺史华轶辟为西曹掾寻轶败悝】 【藏匿轶二子及妻崎岖经年既而遇赦擕之出首帝嘉而宥之】", 
        "唐李邕【江都人尝迁居江夏杜甫 诗称为江夏李邕今县有李邕宅】",
        "元结【字次山河南人代宗时以侍亲丐归寓武昌樊山益着书作 自释一篇】",
        "高骧【幽州人崇文孙性孝嗜学好恬退兄骈为西川节度骧遁去客江淮间爱崇阳山水 卜居之筑愚亭引客赋诗因号愚翁後荆南高季兴过之命图骧像於亭中】", 
        "宋廖正一【字明畧德化 人徙居蒲圻读书凤凰山深造独得黄庭坚深器重之】"]


df = toGPT(text)
print(df)